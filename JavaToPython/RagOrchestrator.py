from typing import List, Optional
import time

from .JsonCorpusLoader import load_corpus
from .RagContext import RagContext
from .TraceEvent import TraceEvent


class RagOrchestrator:
        def __init__(
                self,
                corpus_path: str,
                intent_detector,
                query_writer,
                retriever,
                reranker,
                answer_agent,
                trace_bus,
        ):
                self.corpus = load_corpus(corpus_path)
                self.intent_detector = intent_detector
                self.query_writer = query_writer
                self.retriever = retriever
                self.reranker = reranker
                self.answer_agent = answer_agent
                self.trace_bus = trace_bus
                self.context = RagContext()

        def run(self, question: str) -> None:
                self.context.question = question

                t1 = time.time()
                self.context.intent = self.intent_detector.detect(question)
                t2 = time.time()
                if self.trace_bus:
                        self.trace_bus.on_event(TraceEvent("IntentDetection", question, str(self.context.intent), int((t2 - t1) * 1000)))

                t3 = time.time()
                self.context.terms = self.query_writer.write(question, self.context.intent)
                t4 = time.time()
                if self.trace_bus:
                        self.trace_bus.on_event(TraceEvent("QueryGeneration", question, str(self.context.terms), int((t4 - t3) * 1000)))

                t5 = time.time()
                if callable(self.retriever):
                        self.context.hits = self.retriever(self.context.terms, self.corpus)
                else:
                        self.context.hits = self.retriever.retrieve(self.context.terms, self.corpus)
                t6 = time.time()
                if self.trace_bus:
                        self.trace_bus.on_event(TraceEvent("Retrieval", str(self.context.terms), f"{len(self.context.hits) if self.context.hits else 0} hits", int((t6 - t5) * 1000)))

                t7 = time.time()
                self.context.finalHits = self.reranker.rerank(self.context.terms, self.context.hits)
                t8 = time.time()
                if self.trace_bus:
                        self.trace_bus.on_event(TraceEvent("Reranking", str(self.context.hits), str(self.context.finalHits), int((t8 - t7) * 1000)))

                t9 = time.time()
                self.context.answerText = self.answer_agent.generate_answer(question, self.context.terms, self.context.finalHits)
                t10 = time.time()
                if self.trace_bus:
                        self.trace_bus.on_event(TraceEvent("AnswerGeneration", question, self.context.answerText, int((t10 - t9) * 1000)))

                print(self.context.answerText)

