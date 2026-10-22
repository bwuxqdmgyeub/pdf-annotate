from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from pdf_annotate import PLUGIN_API_VERSION
from pdf_annotate.core.document import DocumentModel


class FormsPlugin:
    plugin_id = "forms"
    display_name = "Forms"
    api_version = PLUGIN_API_VERSION
    enabled_by_default = False

    def activate(self, document: DocumentModel) -> None:
        self._doc = document

    def deactivate(self) -> None:
        self._doc = None  # type: ignore[assignment]

    def fill_field(self, field_name: str, value: str) -> None:
        if not getattr(self, "_doc", None):
            raise RuntimeError("plugin not activated")
        page = self._doc.current_page()
        for widget in page.widgets() or []:
            if widget.field_name == field_name:
                widget.field_value = value
                widget.update()

    def create_panel(self, document: DocumentModel) -> QWidget:
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Fill AcroForm fields on the current page."))
        layout.addStretch(1)
        return panel


PLUGIN = FormsPlugin()