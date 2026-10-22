from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from pdf_annotate.host.bootstrap import build_host


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("PDF Annotate")
    host = build_host()
    host.start()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())