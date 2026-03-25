package mu.cse.rag.clean;

import java.util.Arrays;
import java.util.List;

public class TemplateAnswerAgentTest {
    public static void main(String[] args) {
        TemplateAnswerAgent agent = new TemplateAnswerAgent();

        String text = "İlk cümle. İkinci cümle OOD ve proje kelimelerini içeriyor. Son cümle.";
        Chunk c = new Chunk("docX", 1, "Doc Title", text);
        Hit h = new Hit(c, 10);

        List<String> terms = Arrays.asList("OOD", "proje");
        String answer = agent.generateAnswer("Where is OOD?", terms, Arrays.asList(h));

        boolean hasBest = answer.contains("İkinci cümle OOD ve proje kelimelerini içeriyor");
        boolean hasCitation = answer.contains("Source: Doc Title") && answer.contains("Document: docX");

        System.out.println((hasBest && hasCitation ? "PASS" : "FAIL") + ": TemplateAnswerAgent -> " + answer.replaceAll("\n", " | "));
    }
}
