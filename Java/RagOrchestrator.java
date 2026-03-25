package mu.cse.rag.clean;

import java.util.List;

public class RagOrchestrator {

    private final IntentDetector intentDetector;
    private final QueryWriter queryWriter;
    private final Retriever retriever;
    private final Reranker reranker;
    private final AnswerAgent answerAgent;
    private final List<Chunk> corpus;
    private final TraceBus traceBus;
    private final RagContext context = new RagContext();


    public RagOrchestrator(String corpusPath,
                       IntentDetector intentDetector,
                       QueryWriter queryWriter,
                       Retriever retriever,
                       Reranker reranker,
                       AnswerAgent answerAgent,
                       TraceBus traceBus) {

    this.corpus = JsonCorpusLoader.loadCorpus(corpusPath);
    this.intentDetector = intentDetector;
    this.queryWriter = queryWriter;
    this.retriever = retriever;
    this.reranker = reranker;
    this.answerAgent = answerAgent;
    this.traceBus = traceBus;
}


    public void run(String question) {

    context.question = question;

    // 1) Intent detection
    long t1 = System.currentTimeMillis();
    context.intent = intentDetector.detect(question);
    long t2 = System.currentTimeMillis();
    traceBus.publish(new TraceEvent(
            "IntentDetection",
            question,
            context.intent.toString(),
            t2 - t1
    ));

    // 2) Query generation
    long t3 = System.currentTimeMillis();
    context.terms = queryWriter.write(question, context.intent);
    long t4 = System.currentTimeMillis();
    traceBus.publish(new TraceEvent(
            "QueryGeneration",
            question,
            context.terms.toString(),
            t4 - t3
    ));

    // 3) Retrieval
    long t5 = System.currentTimeMillis();
    context.hits = retriever.retrieve(context.terms, corpus);
    long t6 = System.currentTimeMillis();
    traceBus.publish(new TraceEvent(
            "Retrieval",
            context.terms.toString(),
            (context.hits == null ? "0 hits" : context.hits.size() + " hits"),
            t6 - t5
    ));

    // 4) Reranking
    long t7 = System.currentTimeMillis();
    context.finalHits = reranker.rerank(context.terms, context.hits);
    long t8 = System.currentTimeMillis();
    traceBus.publish(new TraceEvent(
            "Reranking",
            context.hits.toString(),
            context.finalHits.toString(),
            t8 - t7
    ));

    // 5) Answer generation
    long t9 = System.currentTimeMillis();
    context.answerText = answerAgent.generateAnswer(question, context.terms, context.finalHits);
    long t10 = System.currentTimeMillis();
    traceBus.publish(new TraceEvent(
            "AnswerGeneration",
            question,
            context.answerText,
            t10 - t9
    ));

    // 6) Show output
    System.out.println(context.answerText);
}

}
