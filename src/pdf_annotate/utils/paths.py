from __future__ import annotations

import os
from pathlib import Path


def app_data_dir() -> Path:
    base = os.environ.get("LOCALAPPDATA") or os.environ.get("XDG_DATA_HOME")
    root = Path(base) if base else Path.home() / ".local" / "share"
    target = root / "pdf-annotate"
    target.mkdir(parents=True, exist_ok=True)
    return target


def recent_files_path() -> Path:
    return app_data_dir() / "recent.json"