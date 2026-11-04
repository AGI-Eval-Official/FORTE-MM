"""Task loader for MWORK.

Each task is a folder under ``tasks/``:

    <task_id>/
        task.yaml        metadata (id, category, timeout, description)
        instruction.md   the agent's instruction, in its original format
        input/           agent-visible workspace files
        solution/        judge-only reference answers (rubrics.md + more)
        skills/          optional profession skills (land in the agent's HOME)

The loader parses ``task.yaml`` with a deliberately narrow stdlib-only
YAML subset (top-level scalars and string lists — the only shapes our
metadata files use). Everything else (the prompt, the rubric JSON embedded
in ``solution/rubrics.md``, the workspace file list) is derived from the
folder contents at load time, so no generated/duplicated fields are stored
on disk. Full PyYAML behavior is not a goal (D3: host has zero Python
dependencies).
"""

import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional, Any


logger = logging.getLogger(__name__)


def _unquote(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1]
    return s


def _parse_scalar(s: str) -> Any:
    s = s.strip()
    if not s:
        return ""
    if s[0] in ("'", '"') and len(s) >= 2 and s[-1] == s[0]:
        return s[1:-1]
    if s in ("true", "True"):
        return True
    if s in ("false", "False"):
        return False
    if s in ("null", "~", ""):
        return None
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s


def _frontmatter_loads(text: str) -> Dict[str, Any]:
    """Parse the YAML-like frontmatter we actually use.

    Supported shapes:
        key: scalar
        key:
        - scalar
        - scalar
        key:
        - inline_key: value
          inline_key2: value
        - inline_key: value
          ...

    Inline-mapping values are taken verbatim from after the first ':' on the
    line; quotes are stripped if they wrap the whole value. This is enough for
    rubric `content:` fields that contain `<file>...</file>`, full-width
    punctuation, backticks, and embedded `:` characters.
    """
    raw_lines = text.splitlines()
    lines: List[str] = []
    for ln in raw_lines:
        s = ln.rstrip()
        if not s.strip() or s.lstrip().startswith("#"):
            continue
        lines.append(s)

    out: Dict[str, Any] = {}
    i = 0
    n = len(lines)

    while i < n:
        ln = lines[i]
        if not ln or ln[0] in (" ", "-"):
            i += 1
            continue
        key, _, rest = ln.partition(":")
        key = key.strip()
        rest = rest.strip()
        i += 1
        if rest:
            if rest == "[]":
                out[key] = []
            elif rest == "{}":
                out[key] = {}
            else:
                out[key] = _parse_scalar(rest)
            continue
        if i >= n:
            out[key] = None
            continue
        peek = lines[i]
        if peek.startswith("- "):
            # block list at column 0 ("- ...")
            items: List[Any] = []
            while i < n:
                ln2 = lines[i]
                if not ln2.startswith("- "):
                    break
                first = ln2[2:]
                if re.match(r"^[A-Za-z_][\w-]*\s*:", first):
                    item: Dict[str, Any] = {}
                    fkey, _, fval = first.partition(":")
                    item[fkey.strip()] = _parse_scalar(fval.strip()) if fval.strip() else None
                    i += 1
                    while i < n and lines[i].startswith("  ") and not lines[i].startswith("- "):
                        cont = lines[i].lstrip()
                        ckey, _, cval = cont.partition(":")
                        item[ckey.strip()] = _parse_scalar(cval.strip())
                        i += 1
                    items.append(item)
                else:
                    items.append(_parse_scalar(first))
                    i += 1
            out[key] = items
        else:
            out[key] = None

    return out


class Task:
    """A single benchmark task: prompt + assets + grading metadata."""

    def __init__(
        self,
        task_id: str,
        name: str,
        category: str,
        grading_type: str,
        timeout_seconds: int,
        workspace_files: List[Dict[str, str]],
        prompt: str,
        expected_behavior: str,
        grading_criteria: List[str],
        automated_checks: Optional[str] = None,
        llm_judge_rubric: Optional[str] = None,
        grading_weights: Optional[Dict[str, float]] = None,
        file_path: Optional[Path] = None,
        frontmatter: Optional[Dict[str, Any]] = None,
        min_wait_seconds: int = 0,
        task_dir: Optional[Path] = None,
    ):
        self.task_id = task_id
        self.name = name
        self.category = category
        self.grading_type = grading_type
        self.timeout_seconds = timeout_seconds
        self.workspace_files = workspace_files
        self.min_wait_seconds = min_wait_seconds
        self.prompt = prompt
        self.expected_behavior = expected_behavior
        self.grading_criteria = grading_criteria
        self.automated_checks = automated_checks
        self.llm_judge_rubric = llm_judge_rubric
        self.grading_weights = grading_weights
        self.file_path = file_path
        self.frontmatter = frontmatter or {}
        self.task_dir = task_dir or (file_path.parent if file_path else None)

    def __repr__(self) -> str:
        return f"Task(id={self.task_id}, name={self.name}, category={self.category})"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'task_id': self.task_id,
            'name': self.name,
            'category': self.category,
            'grading_type': self.grading_type,
            'timeout_seconds': self.timeout_seconds,
            'workspace_files': self.workspace_files,
            'min_wait_seconds': self.min_wait_seconds,
            'prompt': self.prompt,
            'expected_behavior': self.expected_behavior,
            'grading_criteria': self.grading_criteria,
            'has_automated_checks': self.automated_checks is not None,
            'has_llm_judge_rubric': self.llm_judge_rubric is not None,
            'grading_weights': self.grading_weights,
            'frontmatter': self.frontmatter,
        }


def _extract_rubrics(rubrics_md: str) -> List[Dict[str, Any]]:
    """Extract the embedded rubric JSON array from solution/rubrics.md."""
    match = re.search(r"```json\s*(\[.*?\])\s*```", rubrics_md, re.DOTALL)
    if not match:
        return []
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError:
        return []
    rubrics = []
    for item in data:
        rubrics.append({
            "id": str(item.get("id", "")).strip("'\""),
            "content": str(item.get("content", "")).strip(),
            "weight": item.get("weight", 1),
        })
    return rubrics


def _collect_rubric_file_paths(rubrics: List[Dict[str, Any]]) -> List[str]:
    """Collect unique <file>...</file> targets from rubric contents."""
    seen: List[str] = []
    for rubric in rubrics:
        for m in re.finditer(r"<file>(.*?)</file>", str(rubric.get("content", ""))):
            path = m.group(1).strip()
            if path and path not in seen:
                seen.append(path)
    return seen


def _rel_files(root: Path) -> List[str]:
    if not root.is_dir():
        return []
    return sorted(
        str(p.relative_to(root))
        for p in root.rglob("*")
        if p.is_file() and "__MACOSX" not in p.parts and p.name != ".DS_Store"
    )


class TaskLoader:
    """Loads task folders (`<id>/` containing task.yaml) from a tasks/ dir."""

    def __init__(self, tasks_dir: Path):
        self.tasks_dir = tasks_dir
        logger.info(f"Initialized TaskLoader with directory: {tasks_dir}")

    def load_all_tasks(self) -> List[Task]:
        tasks = []
        task_dirs = sorted(
            p for p in self.tasks_dir.iterdir()
            if p.is_dir() and (p / "task.yaml").exists()
        )
        logger.info(f"Found {len(task_dirs)} task folders")
        for task_dir in task_dirs:
            try:
                task = self.load_task(task_dir)
                tasks.append(task)
                logger.info(f"Successfully loaded task: {task.task_id}")
            except Exception as e:
                logger.error(f"Failed to load task from {task_dir}: {e}", exc_info=True)
        logger.info(f"Successfully loaded {len(tasks)} tasks")
        return tasks

    def load_task(self, task_dir: Path) -> Task:
        logger.debug(f"Loading task from: {task_dir}")
        yaml_path = task_dir / "task.yaml"
        metadata = _frontmatter_loads(yaml_path.read_text(encoding="utf-8"))

        instruction_path = task_dir / "instruction.md"
        if not instruction_path.exists():
            raise ValueError(f"No instruction.md in {task_dir}")
        prompt = instruction_path.read_text(encoding="utf-8").strip()

        # Rubrics live in their original form inside solution/rubrics.md.
        rubrics_md_path = task_dir / "solution" / "rubrics.md"
        rubrics: List[Dict[str, Any]] = []
        if rubrics_md_path.exists():
            rubrics = _extract_rubrics(rubrics_md_path.read_text(encoding="utf-8"))
            if not rubrics:
                logger.warning(f"No rubric JSON found in {rubrics_md_path}")

        # Derived metadata consumed by the runner and the judge.
        metadata = dict(metadata)
        metadata["rubrics"] = rubrics
        metadata["rubric_file_paths"] = _collect_rubric_file_paths(rubrics)
        workspace_files: List[Dict[str, str]] = [
            {"source": f"input/{rel}", "dest": f"input/{rel}"}
            for rel in _rel_files(task_dir / "input")
        ]
        workspace_files += [
            {"source": f"skills/{rel}", "dest": f"skills/{rel}"}
            for rel in _rel_files(task_dir / "skills")
        ]
        metadata["workspace_files"] = workspace_files

        task = Task(
            task_id=metadata.get('id', '') or task_dir.name,
            name=metadata.get('name', '') or task_dir.name,
            category=metadata.get('category', ''),
            grading_type=metadata.get('grading_type', 'llm_judge'),
            timeout_seconds=metadata.get('timeout_seconds', 2400),
            workspace_files=workspace_files,
            min_wait_seconds=metadata.get('min_wait_seconds', 0) or 0,
            prompt=prompt,
            expected_behavior='',
            grading_criteria=[str(r.get("content", "")).strip() for r in rubrics],
            automated_checks=None,
            llm_judge_rubric=None,
            grading_weights=metadata.get('grading_weights', None),
            file_path=yaml_path,
            frontmatter=metadata,
            task_dir=task_dir,
        )
        return task
