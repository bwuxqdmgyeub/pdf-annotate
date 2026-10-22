from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import fitz  # PyMuPDF


@dataclass
class DocumentModel:
    path: Path | None = None
    _doc: fitz.Document | None = field(default=None, repr=False)
    page_index: int = 0

    @property
    def is_open(self) -> bool:
        return self._doc is not None

    @property
    def page_count(self) -> int:
        return self._doc.page_count if self._doc else 0

    def open(self, path: str | Path) -> None:
        self.close()
        self._doc = fitz.open(str(path))
        self.path = Path(path)
        self.page_index = 0

    def close(self) -> None:
        if self._doc is not None:
            self._doc.close()
        self._doc = None
        self.path = None

    def current_page(self) -> fitz.Page:
        if self._doc is None:
            raise RuntimeError("no document open")
        return self._doc.load_page(self.page_index)

    def save(self, out_path: str | Path) -> None:
        if self._doc is None:
            raise RuntimeError("no document open")
        self._doc.save(str(out_path), incremental=False, deflate=True)