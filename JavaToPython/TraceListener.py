from typing import Protocol

from .TraceEvent import TraceEvent


class TraceListener(Protocol):
    def on_event(self, event: TraceEvent) -> None:
        ...

