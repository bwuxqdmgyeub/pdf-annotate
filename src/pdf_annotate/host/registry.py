from __future__ import annotations

from dataclasses import dataclass, field

from pdf_annotate.contracts.plugin import EditorPlugin


@dataclass
class PluginRegistry:
    _plugins: dict[str, EditorPlugin] = field(default_factory=dict)
    _enabled: set[str] = field(default_factory=set)

    def register(self, plugin: EditorPlugin) -> None:
        if plugin.plugin_id in self._plugins:
            raise ValueError(f"duplicate plugin id: {plugin.plugin_id}")
        self._plugins[plugin.plugin_id] = plugin
        if plugin.enabled_by_default:
            self._enabled.add(plugin.plugin_id)

    def get(self, plugin_id: str) -> EditorPlugin | None:
        return self._plugins.get(plugin_id)

    def enabled(self) -> list[EditorPlugin]:
        return [p for pid, p in self._plugins.items() if pid in self._enabled]

    def toggle(self, plugin_id: str, *, on: bool) -> None:
        if plugin_id not in self._plugins:
            raise KeyError(plugin_id)
        if on:
            self._enabled.add(plugin_id)
        else:
            self._enabled.discard(plugin_id)