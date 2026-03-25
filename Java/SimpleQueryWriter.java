package mu.cse.rag.clean;

import java.util.*;

public class SimpleQueryWriter implements QueryWriter {
    
    private final Set<String> stopWords; 
    private final Map<Intent, List<String>> intentBoosters; 
    
    public SimpleQueryWriter() {
        this.stopWords = createStopWords();
        this.intentBoosters = createIntentBoosters();
    }

    @Override 
    public List<String> write(String question, Intent intent) {
        String clearPunctuations = question.toLowerCase(Locale.forLanguageTag("tr-TR"))
                                           .replaceAll("[^a-z0-9üçğıöş\\s]", " "); 
        String[] words = clearPunctuations.split("\\s+"); 
        
        List<String> searchTerms = new ArrayList<>();
        for (String word : words) {
            if (!stopWords.contains(word) && word.length() > 2) {
                searchTerms.add(word);
            }
        }

        	
        List<String> boosters = intentBoosters.get(intent); 
        if (boosters != null) {
            for (String booster : boosters) {
                if (!searchTerms.contains(booster)) {
                    searchTerms.add(booster);
                }
            }
        }
        return searchTerms;
    }

    private Set<String> createStopWords() {
        Set<String> stops = new HashSet<>();
        stops.add("ve"); stops.add("ile"); stops.add("bu"); stops.add("şu");
        stops.add("bir"); stops.add("nedir"); stops.add("nasıl"); stops.add("hangi");
        stops.add("için"); stops.add("ama"); stops.add("fakat"); stops.add("lakin");
        stops.add("mi"); stops.add("mı"); stops.add("mu"); stops.add("mü");
        return stops;
    }

    private Map<Intent, List<String>> createIntentBoosters() {
        Map<Intent, List<String>> boosters = new HashMap<>();

        List<String> staffTerms = new ArrayList<>();
        staffTerms.add("öğretim"); staffTerms.add("hoca"); staffTerms.add("ofis");
        staffTerms.add("telefon"); staffTerms.add("öğretmen"); staffTerms.add("akademisyen");
        boosters.put(Intent.STAFF_LOOKUP, staffTerms);
        
        List<String> courseTerms = new ArrayList<>();
        courseTerms.add("ders"); courseTerms.add("kredi"); courseTerms.add("önkoşul");
        courseTerms.add("dönem"); courseTerms.add("müfredat"); 
        boosters.put(Intent.COURSE, courseTerms);
        
        List<String> policyTerms = new ArrayList<>();
        policyTerms.add("yönerge"); policyTerms.add("kural"); policyTerms.add("sınav");
        policyTerms.add("not"); policyTerms.add("madde"); 
        boosters.put(Intent.POLICY_FAQ, policyTerms); 

        List<String> regTerms = new ArrayList<>();
        regTerms.add("kayıt"); regTerms.add("başvuru"); regTerms.add("öğrenci");
        regTerms.add("kabul"); regTerms.add("belge"); regTerms.add("ücret");
        boosters.put(Intent.REGISTRATION, regTerms);
        
        return boosters;
    }
}