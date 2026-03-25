from typing import List, Protocol


class AnswerAgent(Protocol):
    #Implements Protocol for a string return
    def generate_answer(self, question: str, terms: List[str], hits: List['Hit']) -> str:
        ...

