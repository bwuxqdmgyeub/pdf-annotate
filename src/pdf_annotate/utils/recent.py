from __future__ import annotations

import json
from pathlib import Path

from pdf_annotate.utils.paths import recent_files_path

MAX_RECENT = 15


def load_recent() -> list[str]:
    path = recent_files_path()
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    return [str(p) for p in data if isinstance(p, str)][:MAX_RECENT]


def push_recent(pdf_path: str | Path) -> list[str]:
    resolved = str(Path(pdf_path).resolve())
    items = [p for p in load_recent() if p != resolved]
    items.insert(0, resolved)
    items = items[:MAX_RECENT]
    recent_files_path().write_text(json.dumps(items, indent=2), encoding="utf-8")
    return items