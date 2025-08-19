import re

class EthiopianTextCleaner:
    """
    A utility class for cleaning Ethiopian text data 
    (Amharic, Geez, and related languages).
    """

    def __init__(self, lower: bool = True, remove_punctuation: bool = True):
        self.lower = lower
        self.remove_punctuation = remove_punctuation

        # Common unwanted symbols/punctuations
        self.punctuation_pattern = r"[!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~።፣፤፥፦፧፨]"

    def clean_text(self, text: str) -> str:
        """Clean and normalize Ethiopian text."""
        # Normalize spaces
        text = re.sub(r"\s+", " ", text).strip()

        # Remove punctuation
        if self.remove_punctuation:
            text = re.sub(self.punctuation_pattern, "", text)

        # Lowercasing (Amharic/Geez scripts don't have true case, 
        # but English mix-ins do)
        if self.lower:
            text = text.lower()

        return text

    def clean_corpus(self, texts: list) -> list:
        """Apply cleaning across a list of texts."""
        return [self.clean_text(t) for t in texts]
import re

class EthiopianTextCleaner:
    def __init__(self, lower=True, remove_punctuation=True, normalize_numerals=True):
        self.lower = lower
        self.remove_punctuation = remove_punctuation
        self.normalize_numerals = normalize_numerals

        # Common punctuation & separators
        self.punctuation_pattern = r"[!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~።፣፤፥፦፧፨]"

    def normalize_geez_numerals(self, text: str) -> str:
        mapping = {
            "፩": "1", "፪": "2", "፫": "3", "፬": "4", "፭": "5",
            "፮": "6", "፯": "7", "፰": "8", "፱": "9", "፲": "10",
        }
        for geez, arabic in mapping.items():
            text = text.replace(geez, arabic)
        return text

    def clean_text(self, text: str) -> str:
        # Normalize whitespace
        text = re.sub(r"\s+", " ", text).strip()

        # Remove punctuation
        if self.remove_punctuation:
            text = re.sub(self.punctuation_pattern, "", text)

        # Lowercase (mainly for English parts)
        if self.lower:
            text = text.lower()

        # Normalize numerals if requested
        if self.normalize_numerals:
            text = self.normalize_geez_numerals(text)

        return text

    def clean_corpus(self, texts: list) -> list:
        return [self.clean_text(t) for t in texts]
