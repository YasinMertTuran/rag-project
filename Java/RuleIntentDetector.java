package mu.cse.rag.clean;

import java.util.Locale;

public class RuleIntentDetector implements IntentDetector {
    @Override
    public Intent detect(String question) {
        String q = question.toLowerCase(Locale.forLanguageTag("tr-TR"));
        
        for (Intent intent : Intent.values()) {
            if (intent == Intent.UNKNOWN) continue;
                for (String keyword : intent.getKeywords()) {
                    if (q.contains(keyword)) {
                    return intent;
                    }
            }
        }
        return Intent.UNKNOWN;
    }
}