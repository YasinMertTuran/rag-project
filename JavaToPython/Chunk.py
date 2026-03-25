from dataclasses import dataclass

@dataclass
class Chunk:
    docId: str
    id: int
    title: str
    text: str

