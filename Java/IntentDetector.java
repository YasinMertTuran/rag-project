package mu.cse.rag.clean;

public interface IntentDetector {
    Intent detect(String question);
}