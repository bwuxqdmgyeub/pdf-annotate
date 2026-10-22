from __future__ import annotations

from PySide6.QtWidgets import (
    QMainWindow,
    QTabWidget,
    QToolBar,
    QWidget,
)

from pdf_annotate.core.document import DocumentModel
from pdf_annotate.host.registry import PluginRegistry


class MainWindow(QMainWindow):
    def __init__(self, registry: PluginRegistry, document: DocumentModel) -> None:
        super().__init__()
        self._registry = registry
        self._document = document
        self.setWindowTitle("PDF Annotate")
        self.resize(1280, 860)

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        toolbar = QToolBar("Plugins", self)
        for plugin in registry.enabled():
            action = toolbar.addAction(plugin.display_name)
            action.triggered.connect(
                lambda _checked=False, p=plugin: self._open_plugin_panel(p)
            )
        self.addToolBar(toolbar)

    def _open_plugin_panel(self, plugin) -> None:  # type: ignore[no-untyped-def]
        panel: QWidget = plugin.create_panel(self._document)
        self.tabs.addTab(panel, plugin.display_name)
        self.tabs.setCurrentWidget(panel)