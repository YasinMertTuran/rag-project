from .TemplateAnswerAgent import TemplateAnswerAgent
from .Chunk import Chunk
from .Hit import Hit


def run_test():
    agent = TemplateAnswerAgent()
    text = "İlk cümle. İkinci cümle OOD ve proje kelimelerini içeriyor. Son cümle."
    c = Chunk("docX", 1, "Doc Title", text)
    h = Hit(c, 10)
    terms = ["OOD", "proje"]
    answer = agent.generate_answer("Where is OOD?", terms, [h])
    has_best = "İkinci cümle OOD ve proje kelimelerini içeriyor" in answer
    has_citation = "Source: Doc Title" in answer and "Document: docX" in answer
    print(("PASS" if (has_best and has_citation) else "FAIL") + ": TemplateAnswerAgent -> " + answer.replace("\n", " | "))


if __name__ == "__main__":
    run_test()

