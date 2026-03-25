from typing import List, Protocol
from .Intent import Intent

class QueryWriter(Protocol):
    def write(self, question: str, intent: Intent) -> List[str]:
        ...

