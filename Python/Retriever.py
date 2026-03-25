from typing import Protocol, List


class Retriever(Protocol):
    def retrieve(self, terms: List[str], corpus: List['Chunk']) -> List['Hit']:
        ...

