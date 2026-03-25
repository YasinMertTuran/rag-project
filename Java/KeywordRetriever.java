package mu.cse.rag.clean;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;

public class KeywordRetriever implements Retriever {
    @Override
    public List<Hit> retrieve(List<String> terms, List<Chunk> corpus) {
        List<Hit> hits = new ArrayList<>();
        
        for (Chunk chunk : corpus) {
            int score = 0;
            String content = chunk.text.toLowerCase(Locale.forLanguageTag("tr-TR")); 
            
            for (String term : terms) {
                if (content.contains(term)) {
                    score += 1;
                }
            }
            if (score > 0) {
                hits.add(new Hit(chunk, score));
            }
        }
        hits.sort((h1, h2) -> Integer.compare(h2.score, h1.score)); //Sort by score (descending)
        return hits.stream().limit(5).collect(Collectors.toCollection(ArrayList::new)); //Return top 5 hits
    }
}