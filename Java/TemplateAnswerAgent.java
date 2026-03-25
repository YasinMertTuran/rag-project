package mu.cse.rag.clean;

import java.util.List;

public class TemplateAnswerAgent implements AnswerAgent {

    @Override
    public String generateAnswer(String question, List<String> terms, List<Hit> hits) {
        if (hits == null || hits.isEmpty()) {
            return "No information found for the given question.";
        }

        Hit best = hits.get(0); //Take the top hit
        Chunk chunk = best.chunk; //Get the chunk from the hit

        String bestSentence = findBestSentence(chunk.text, terms);

        StringBuilder sb = new StringBuilder(); //String builder for answer
        sb.append(bestSentence).append("\n"); //Best sentence found
        sb.append("--------------------------------------------------\n"); //Separating line for clarity
        sb.append("Source: ").append(chunk.title) 
          .append(" | Document: ").append(chunk.docId);

        return sb.toString();
    }

    
    private String findBestSentence(String text, List<String> terms) {
        if (text == null || text.isEmpty()) {
            return "No relevant sentence found.";
        }

        String[] sentences = text.split("(?<=[.!?])\\s+"); //Split by sentence-ending punctuation

        String bestSentence = sentences[0];
        int bestScore = -1;

        for (String sentence : sentences) {
        
            int score = 0;
            String lower = sentence.toLowerCase();
            for (String term : terms) {
                if (term == null || term.isBlank()) continue;
                if (lower.contains(term.toLowerCase())) {
                    score++;
                }
            }
            if (score > bestScore) { //Higher score found
                bestScore = score;  //Update best score
                bestSentence = sentence; //Update best sentence
            }
        }
        return bestSentence;
    }
}
