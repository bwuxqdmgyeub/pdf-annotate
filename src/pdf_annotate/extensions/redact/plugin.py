from __future__ import annotations

import fitz
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from pdf_annotate import PLUGIN_API_VERSION
from pdf_annotate.core.document import DocumentModel


class RedactPlugin:
    plugin_id = "redact"
    display_name = "Redact"
    api_version = PLUGIN_API_VERSION
    enabled_by_default = True

    def activate(self, document: DocumentModel) -> None:
        self._doc = document

    def deactivate(self) -> None:
        self._doc = None  # type: ignore[assignment]

    def apply(self, rect: fitz.Rect) -> None:
        if not getattr(self, "_doc", None):
            raise RuntimeError("plugin not activated")
        page = self._doc.current_page()
        page.add_redact_annot(rect, fill=(0, 0, 0))
        page.apply_redactions()

    def create_panel(self, document: DocumentModel) -> QWidget:
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Draw a rectangle to permanently redact content."))
        layout.addStretch(1)
        return panel


PLUGIN = RedactPlugin()