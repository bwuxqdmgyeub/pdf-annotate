from __future__ import annotations

from typing import Protocol, runtime_checkable

from PySide6.QtWidgets import QWidget

from pdf_annotate.core.document import DocumentModel


@runtime_checkable
class EditorPlugin(Protocol):
    """Every extension module implements this contract."""

    plugin_id: str
    display_name: str
    api_version: int
    enabled_by_default: bool

    def activate(self, document: DocumentModel) -> None: ...
    def deactivate(self) -> None: ...
    def create_panel(self, document: DocumentModel) -> QWidget: ...


class PluginApiMismatch(RuntimeError):
    pass