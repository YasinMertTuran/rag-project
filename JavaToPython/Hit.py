from dataclasses import dataclass

@dataclass
class Hit:
    chunk: 'Chunk'
    score: int

