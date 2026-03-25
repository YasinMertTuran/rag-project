from dataclasses import dataclass
from typing import List, Optional
from .Intent import Intent


@dataclass
class RagContext:
    question: Optional[str] = None
    intent: Optional[Intent] = None
    terms: Optional[List[str]] = None
    hits: Optional[List['Hit']] = None
    finalHits: Optional[List['Hit']] = None
    answerText: Optional[str] = None

