from __future__ import annotations

import importlib
import importlib.metadata as md
from typing import Iterable

from pdf_annotate import PLUGIN_API_VERSION
from pdf_annotate.contracts.plugin import EditorPlugin, PluginApiMismatch

_BUILTIN = [
    "pdf_annotate.extensions.highlight",
    "pdf_annotate.extensions.redact",
    "pdf_annotate.extensions.forms",
    "pdf_annotate.extensions.ocr",
]


def _load_module(dotted: str) -> EditorPlugin | None:
    try:
        mod = importlib.import_module(dotted)
    except ImportError:
        return None
    plugin = getattr(mod, "PLUGIN", None)
    if plugin is None:
        return None
    if plugin.api_version != PLUGIN_API_VERSION:
        raise PluginApiMismatch(
            f"{dotted}: expected api {PLUGIN_API_VERSION}, got {plugin.api_version}"
        )
    return plugin


def discover_plugins() -> Iterable[EditorPlugin]:
    seen: set[str] = set()
    for dotted in _BUILTIN:
        plugin = _load_module(dotted)
        if plugin and plugin.plugin_id not in seen:
            seen.add(plugin.plugin_id)
            yield plugin

    try:
        eps = md.entry_points(group="pdf_annotate.plugins")
    except TypeError:
        eps = md.entry_points().get("pdf_annotate.plugins", [])

    for ep in eps:
        try:
            plugin = ep.load()
        except Exception:
            continue
        if plugin.plugin_id in seen:
            continue
        seen.add(plugin.plugin_id)
        yield plugin