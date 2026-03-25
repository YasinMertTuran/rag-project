package mu.cse.rag.clean;

import java.util.List;

public class QueryWriterTests {
    public static void main(String[] args) {
        SimpleQueryWriter writer = new SimpleQueryWriter();

        testStopwordRemoval(writer);
        testIntentBoosters(writer);
        testStemmingBehavior(writer);
    }

    private static void testStopwordRemoval(SimpleQueryWriter writer) {
        String q = "Bu ders nedir ve nasıl alınır?";
        List<String> terms = writer.write(q, Intent.COURSE);
        boolean pass = true;
        String[] stops = {"bu", "nedir", "nasıl", "ve"};
        for (String s : stops) {
            if (terms.contains(s)) {
                pass = false;
            }
        }
        System.out.println((pass ? "PASS" : "FAIL") + ": Stopword removal -> " + terms);
    }

    private static void testIntentBoosters(SimpleQueryWriter writer) {
        String q = "Bilgi";
        List<String> courseTerms = writer.write(q, Intent.COURSE);
        boolean hasBooster = courseTerms.contains("ders") || courseTerms.contains("kredi");
        System.out.println((hasBooster ? "PASS" : "FAIL") + ": Course -> " + courseTerms);

        List<String> staffTerms = writer.write(q, Intent.STAFF_LOOKUP);
        boolean hasStaff = staffTerms.contains("öğretim") || staffTerms.contains("hoca");
        System.out.println((hasStaff ? "PASS" : "FAIL") + ": Staff -> " + staffTerms);
    }

    private static void testStemmingBehavior(SimpleQueryWriter writer) {
        String q = "Öğretmenleri bulmak istiyorum";
        List<String> terms = writer.write(q, Intent.STAFF_LOOKUP);
        boolean containsInflected = terms.stream().anyMatch(t -> t.contains("öğretmen"));
        boolean containsBoosterBase = terms.contains("öğretmen") || terms.contains("öğretim");
        boolean pass = containsInflected && containsBoosterBase;
        System.out.println((pass ? "PASS" : "FAIL") + ": terms=" + terms);
    }
}
