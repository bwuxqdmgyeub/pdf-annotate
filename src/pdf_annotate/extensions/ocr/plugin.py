from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from pdf_annotate import PLUGIN_API_VERSION
from pdf_annotate.core.document import DocumentModel


class OcrPlugin:
    plugin_id = "ocr"
    display_name = "OCR"
    api_version = PLUGIN_API_VERSION
    enabled_by_default = False

    def activate(self, document: DocumentModel) -> None:
        self._doc = document

    def deactivate(self) -> None:
        self._doc = None  # type: ignore[assignment]

    def extract_text(self, dpi: int = 300) -> str:
        if not getattr(self, "_doc", None):
            raise RuntimeError("plugin not activated")
        page = self._doc.current_page()
        pix = page.get_pixmap(dpi=dpi)
        tmp = Path("ocr_page.png")
        pix.save(str(tmp))
        # Real OCR backend is plugged in at build time; stub returns empty.
        return ""

    def create_panel(self, document: DocumentModel) -> QWidget:
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Run OCR on the current page to extract text."))
        layout.addStretch(1)
        return panel


PLUGIN = OcrPlugin()