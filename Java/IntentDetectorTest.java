package mu.cse.rag.clean;

public class IntentDetectorTest {
    public static void main(String[] args) {
        IntentDetector detector = new RuleIntentDetector();

        expect("Kayıt ve hoca bilgilerini nereden alabilirim?", Intent.REGISTRATION, detector);
        expect("Hoca e-posta ve yönergeler nerede?", Intent.STAFF_LOOKUP, detector);
        expect("Yönerge ve ders ile ilgili soru", Intent.POLICY_FAQ, detector);
        expect("Bu tamamen bilgilendirici bir cümle.", Intent.UNKNOWN, detector);
    }

    private static void expect(String question, Intent expected, IntentDetector detector) {
        Intent found = detector.detect(question);
        if (found == expected) {
            System.out.println("PASS: " + question + " -> " + found);
        } else {
            System.out.println("FAIL: " + question + " -> " + found + " (expected " + expected + ")");
        }
    }
}
