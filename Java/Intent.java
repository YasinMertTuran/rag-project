package mu.cse.rag.clean;

public enum Intent {
    REGISTRATION("kayıt", "başvuru", "harç", "ücret", "belge"),
    STAFF_LOOKUP("öğretim", "hoca", "akademisyen", "ofis", "mail", "telefon"),
    POLICY_FAQ("yönerge", "mevzuat", "kural", "politika", "sınav", "not", "yönetmelik", "madde"),
    COURSE("ders", "kurs", "müfredat", "kredi", "akts", "önkoşul"),
    UNKNOWN("bilinmeyen");
    
    private final String[] keywords;
    
    Intent(String... keywords) {
        this.keywords = keywords;
    }
    
    public String[] getKeywords() {
        return keywords;
    }
}