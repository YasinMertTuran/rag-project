package mu.cse.rag.clean;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class SimpleReranker implements Reranker {
	@Override
    public List<Hit> rerank(List<String> terms, List<Hit> hits) {
        List<Hit> mutableHits = new ArrayList<>(hits);

        for (Hit hit : mutableHits) {
            String title = hit.chunk.title.toLowerCase(Locale.forLanguageTag("tr-TR"));
            String text = hit.chunk.text.toLowerCase(Locale.forLanguageTag("tr-TR"));
            int score = 0; 
  
            for (String term : terms) { //Add points for each term found
                if (text.contains(term)) {
                    score += 1;
                }
                if (title.contains(term)) { //Add more points for title matches
                    score += 3;
                }
            }

            String query = String.join(" ", terms);
            if (text.contains(query)) {
                score += 5; 
            }
            hit.score = score;
        }

        mutableHits.sort((h1, h2) -> Integer.compare(h2.score, h1.score));
        return mutableHits;
    }
}