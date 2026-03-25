from typing import List, Protocol


class Reranker(Protocol):
    def rerank(self, terms: List[str], hits: List['Hit']) -> List['Hit']:
        ...

