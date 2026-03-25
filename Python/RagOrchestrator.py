from typing import List, Optional
import time
from .JsonCorpusLoader import load_corpus
from .RagContext import RagContext
from .TraceEvent import TraceEvent

class RagOrchestrator:
    def __init__(self, corpus_path, intent_detector, query_writer, retriever, reranker, answer_agent, trace_bus):
        self.corpus = load_corpus(corpus_path)
        self.intent_detector = intent_detector
        self.query_writer = query_writer
        self.retriever = retriever
        self.reranker = reranker
        self.answer_agent = answer_agent
        self.trace_bus = trace_bus
        self.context = RagContext() 
        # Raporlama için metrikleri burada tutuyoruz
        self.last_latency_ms = 0
        self.last_success = False

    def run(self, question: str) -> None:
        start_time = time.perf_counter() # Hassas zamanlama başlangıcı
        
        self.context = RagContext()
        self.context.question = question

        # 1. Intent Detection
        self.context.intent = self.intent_detector.detect(question) 
        
        # 2. Query Generation
        self.context.terms = self.query_writer.write(question, self.context.intent)
        
        # 3. Retrieval
        if hasattr(self.retriever, 'retrieve'):
            self.context.hits = self.retriever.retrieve(self.context.terms, self.corpus) 
        else:
            self.context.hits = self.retriever(self.context.terms, self.corpus)
            
        # 4. Reranking
        self.context.finalHits = self.reranker.rerank(self.context.terms, self.context.hits)
        
        # 5. Answer Generation
        self.context.answerText = self.answer_agent.generate_answer(question, self.context.terms, self.context.finalHits)
        
        # Metrikleri kaydet
        end_time = time.perf_counter()
        self.last_latency_ms = int((end_time - start_time) * 1000)
        self.last_success = len(self.context.finalHits) > 0

        # Cevabı bas
        print(self.context.answerText)

        # 6. Trace Loglarını Kaydet
        if self.trace_bus:
            self.trace_bus.on_event(TraceEvent("FullPipeline", question, "Success", self.last_latency_ms))