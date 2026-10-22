from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from pdf_annotate.core.document import DocumentModel


@dataclass(frozen=True)
class DocumentOpened:
    path: str
    page_count: int


@dataclass(frozen=True)
class AnnotationCommitted:
    page_index: int
    kind: str


EventHandler = Callable[[object], None]


class EventBus:
    def __init__(self) -> None:
        self._subs: dict[type, list[EventHandler]] = {}

    def subscribe(self, event_type: type, handler: EventHandler) -> None:
        self._subs.setdefault(event_type, []).append(handler)

    def publish(self, event: object) -> None:
        for handler in self._subs.get(type(event), []):
            handler(event)


__all__ = [
    "DocumentOpened",
    "AnnotationCommitted",
    "EventBus",
    "DocumentModel",
]