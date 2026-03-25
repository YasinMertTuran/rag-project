package mu.cse.rag.clean;

import java.util.List;

public interface AnswerAgent {
    String generateAnswer(String question, List<String> terms, List<Hit> hits); //Generates answer based on question and hits
}
