from __future__ import annotations

import fitz

from pdf_annotate.core.document import DocumentModel


def add_highlight(
    document: DocumentModel,
    rect: fitz.Rect,
    *,
    color: tuple[float, float, float] = (1.0, 0.92, 0.23),
) -> fitz.Annot:
    page = document.current_page()
    annot = page.add_highlight_annot(rect)
    annot.set_colors(stroke=color)
    annot.update()
    return annot


def add_text_note(
    document: DocumentModel,
    point: fitz.Point,
    text: str,
) -> fitz.Annot:
    page = document.current_page()
    annot = page.add_text_annot(point, text)
    annot.update()
    return annot


def add_sticky_rect(
    document: DocumentModel,
    rect: fitz.Rect,
    *,
    stroke: tuple[float, float, float] = (0.9, 0.2, 0.2),
) -> fitz.Annot:
    page = document.current_page()
    annot = page.add_rect_annot(rect)
    annot.set_colors(stroke=stroke)
    annot.set_border(width=1.5)
    annot.update()
    return annot