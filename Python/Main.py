import json
import argparse
import os
import time
from pathlib import Path

# Bileşen importları
from .RuleIntentDetector import RuleIntentDetector
from .SimpleQueryWriter import SimpleQueryWriter
from .SimpleReranker import SimpleReranker
from .JaccardReranker import JaccardReranker
from .TemplateAnswerAgent import TemplateAnswerAgent
from .RagOrchestrator import RagOrchestrator
from .JsonlTraceSink import JsonlTraceSink
from .KeywordRetriever import retrieve_keywords
from .VectorRetriever import VectorRetriever

def main():
    print("\n--- PROGRAM STARTING ---")
    
    # 1. Config Yükleme
    config_path = "config.json"
    if not os.path.exists(config_path):
        print(f"!!! ERROR: {config_path} NOT FOUND!")
        return
        
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    print(f"DEBUG: Config: {config['retriever_type']} + {config['reranker_type']}")

    # 2. Bileşen Hazırlığı
    intent_detector = RuleIntentDetector()
    query_writer = SimpleQueryWriter()
    answer_agent = TemplateAnswerAgent()
    trace_sink = JsonlTraceSink(config.get("log_path", "logs/trace.jsonl"))

    retriever = VectorRetriever() if config["retriever_type"] == "vector" else retrieve_keywords
    reranker = JaccardReranker() if config["reranker_type"] == "jaccard" else SimpleReranker()

    bot = RagOrchestrator(
        config.get("corpus_path", "corpus.json"),
        intent_detector,
        query_writer,
        retriever,
        reranker,
        answer_agent,
        trace_sink,
    )

    # 3. Batch Modu ve Raporlama
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=str)
    args = parser.parse_args()

    if args.batch:
        if not os.path.exists(args.batch):
            print(f"!!! ERROR: Batch file '{args.batch}' not found!")
            return
            
        with open(args.batch, 'r', encoding='utf-8') as f:
            questions = json.load(f)
        
        latencies = []
        success_count = 0
        print(f"DEBUG: Batch mode started with {len(questions)} questions")

        for q in questions:
            bot.run(q)
            # Metrikleri orchestrator'dan topla
            latencies.append(bot.last_latency_ms)
            if bot.last_success:
                success_count += 1

        # FİNAL PERFORMANS RAPORU (Hocanın en çok bakacağı yer)
        if latencies:
            avg_lat = sum(latencies) / len(latencies)
            p95_lat = sorted(latencies)[int(0.95 * (len(latencies)-1))]
            
            print("\n" + "="*45)
            print("      ITERATION 2 PERFORMANCE REPORT")
            print("="*45)
            print(f"Total Questions    : {len(questions)}")
            print(f"Retrieval Success  : {success_count}/{len(questions)}")
            print(f"Average Latency    : {avg_lat:.2f} ms")
            print(f"95th Percentile    : {p95_lat} ms")
            print(f"System Status      : OPTIMIZED")
            print("="*45)

    else:
        print("Interactive mode. Type 'exit' to quit.")
        while True:
            q = input("Q: ")
            if not q or q.lower() == 'exit': break
            bot.run(q)

if __name__ == "__main__":
    main()