from __future__ import annotations

from pathlib import Path

from pdf_annotate.utils import recent


def test_push_recent_dedupes(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(recent, "recent_files_path", lambda: tmp_path / "recent.json")
    a = tmp_path / "a.pdf"
    b = tmp_path / "b.pdf"
    a.write_bytes(b"%PDF-1.4\n")
    b.write_bytes(b"%PDF-1.4\n")

    recent.push_recent(a)
    recent.push_recent(b)
    items = recent.push_recent(a)
    assert items[0] == str(a.resolve())
    assert len(items) == 2
</｜｜DSML｜｜ parameter>