from __future__ import annotations

from pdf_annotate.contracts.plugin import EditorPlugin
from pdf_annotate.core.document import DocumentModel
from pdf_annotate.extensions.loader import discover_plugins
from pdf_annotate.host.registry import PluginRegistry
from pdf_annotate.host.window import MainWindow


class EditorHost:
    def __init__(self, registry: PluginRegistry, document: DocumentModel) -> None:
        self.registry = registry
        self.document = document
        self.window: MainWindow | None = None

    def start(self) -> None:
        self.window = MainWindow(self.registry, self.document)
        self.window.show()


def build_host() -> EditorHost:
    registry = PluginRegistry()
    for plugin in discover_plugins():
        registry.register(plugin)
    document = DocumentModel()
    return EditorHost(registry, document)


__all__ = ["EditorHost", "build_host", "EditorPlugin"]