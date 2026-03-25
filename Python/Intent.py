from enum import Enum
from typing import Tuple

class Intent(Enum):
    REGISTRATION = ("kayıt", "başvuru", "harç", "ücret", "belge")
    STAFF_LOOKUP = ("öğretim", "hoca", "akademisyen", "ofis", "mail", "telefon")
    POLICY_FAQ = ("yönerge", "mevzuat", "kural", "politika", "sınav", "not", "yönetmelik", "madde")
    COURSE = ("ders", "kurs", "müfredat", "kredi", "akts", "önkoşul")
    UNKNOWN = ("bilinmeyen",)

    def __init__(self, *keywords: str):
        self._keywords: Tuple[str, ...] = keywords

    def get_keywords(self) -> Tuple[str, ...]:
        return self._keywords

