from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from pdf_annotate import PLUGIN_API_VERSION
from pdf_annotate.core.document import DocumentModel


class HighlightPlugin:
    plugin_id = "highlight"
    display_name = "Highlight"
    api_version = PLUGIN_API_VERSION
    enabled_by_default = True

    def activate(self, document: DocumentModel) -> None:
        self._doc = document

    def deactivate(self) -> None:
        self._doc = None  # type: ignore[assignment]

    def create_panel(self, document: DocumentModel) -> QWidget:
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Drag on the page to add a highlight annotation."))
        layout.addStretch(1)
        return panel


PLUGIN = HighlightPlugin()