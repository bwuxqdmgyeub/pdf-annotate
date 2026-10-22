from __future__ import annotations

from pdf_annotate.contracts.plugin import EditorPlugin
from pdf_annotate.host.registry import PluginRegistry


class _Stub:
    plugin_id = "stub"
    display_name = "Stub"
    api_version = 3
    enabled_by_default = True

    def activate(self, document) -> None: ...
    def deactivate(self) -> None: ...
    def create_panel(self, document):  # pragma: no cover - trivial
        return None


def test_register_and_toggle() -> None:
    reg = PluginRegistry()
    reg.register(_Stub())  # type: ignore[arg-type]
    assert [p.plugin_id for p in reg.enabled()] == ["stub"]
    reg.toggle("stub", on=False)
    assert reg.enabled() == []
    assert isinstance(reg.get("stub"), EditorPlugin)


def test_duplicate_id_rejected() -> None:
    reg = PluginRegistry()
    reg.register(_Stub())  # type: ignore[arg-type]
    try:
        reg.register(_Stub())  # type: ignore[arg-type]
    except ValueError:
        return
    raise AssertionError("expected ValueError on duplicate plugin id")