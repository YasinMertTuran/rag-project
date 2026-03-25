package mu.cse.rag.clean;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        IntentDetector intentDetector = new RuleIntentDetector();
        QueryWriter queryWriter = new SimpleQueryWriter();
        Retriever retriever = new KeywordRetriever();
        Reranker reranker = new SimpleReranker();
        AnswerAgent answerAgent = new TemplateAnswerAgent();
        TraceBus traceBus = new TraceBus();

        traceBus.addListener(new JsonlTraceSink("logs/trace.jsonl"));

        RagOrchestrator bot = new RagOrchestrator(
                "data/corpus.json",
                intentDetector,
                queryWriter,
                retriever,
                reranker,
                answerAgent,
                traceBus
        );

        System.out.println("Enter your question(Type exit to quit)\n");

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Question: ");
            String input = scanner.nextLine();
            if ("exit".equalsIgnoreCase(input.trim())) break;
            bot.run(input);
        }
        scanner.close();
    }
}
