from typing import Protocol
from .Intent import Intent


class IntentDetector(Protocol):
    def detect(self, question: str) -> Intent:
        ...

