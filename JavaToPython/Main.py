from .RuleIntentDetector import RuleIntentDetector
from .SimpleQueryWriter import SimpleQueryWriter
from .SimpleReranker import SimpleReranker
from .TemplateAnswerAgent import TemplateAnswerAgent
from .RagOrchestrator import RagOrchestrator
from .JsonlTraceSink import JsonlTraceSink
from .KeywordRetriever import retrieve_keywords
import os
from pathlib import Path


def main():
    intent_detector = RuleIntentDetector()
    query_writer = SimpleQueryWriter()
    reranker = SimpleReranker()
    answer_agent = TemplateAnswerAgent()

    trace_sink = JsonlTraceSink("logs/trace.jsonl")

    # Resolve corpus path: prefer working-dir relative path, otherwise try project-root/data/corpus.json
    corpus_rel = "data/corpus.json"
    corpus_path = corpus_rel
    if not os.path.isabs(corpus_path) and not os.path.exists(corpus_path):
        try:
            # file is in src/mu/cse/rag/clean; project root is 5 parents up
            project_root = Path(__file__).resolve().parents[5]
            alt = project_root / 'data' / 'corpus.json'
            if alt.exists():
                corpus_path = str(alt)
        except Exception:
            pass

    bot = RagOrchestrator(
        corpus_path,
        intent_detector,
        query_writer,
        retrieve_keywords,  # use keyword-based retriever by default
        reranker,
        answer_agent,
        trace_sink,
    )

    print("Enter your question(Type exit to quit)\n")
    try:
        while True:
            input_q = input("Question: ")
            if input_q.strip().lower() == 'exit':
                break
            bot.run(input_q)
    except (KeyboardInterrupt, EOFError):
        print('\nExiting')


if __name__ == "__main__":
    main()

