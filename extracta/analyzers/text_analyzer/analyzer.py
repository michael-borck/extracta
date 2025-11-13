import re
from collections import Counter
from typing import List, Dict, Any


class TextAnalyzer:
    """Research and assessment focused text analysis"""

    # Basic sentiment word lists
    POSITIVE_WORDS = {
        "good",
        "great",
        "excellent",
        "amazing",
        "wonderful",
        "fantastic",
        "love",
        "like",
        "enjoy",
        "happy",
        "pleased",
        "satisfied",
        "best",
        "better",
        "perfect",
        "awesome",
        "brilliant",
    }

    NEGATIVE_WORDS = {
        "bad",
        "terrible",
        "awful",
        "horrible",
        "hate",
        "dislike",
        "sad",
        "angry",
        "frustrated",
        "disappointed",
        "worst",
        "worse",
        "poor",
        "ugly",
        "stupid",
        "dumb",
        "annoying",
    }

    def analyze(self, text: str, mode: str = "assessment") -> dict:
        if mode == "research":
            return self._research_analysis(text)
        else:
            return self._assessment_analysis(text)

    def _research_analysis(self, text: str) -> dict:
        return {
            "themes": self._extract_themes(text),
            "discourse_patterns": self._analyze_discourse(text),
            "sentiment": self._analyze_sentiment(text),
            "linguistic_features": self._analyze_linguistics(text),
        }

    def _assessment_analysis(self, text: str) -> dict:
        return {
            "readability": self._analyze_readability(text),
            "writing_quality": self._analyze_quality(text),
            "vocabulary_richness": self._analyze_vocabulary(text),
            "grammar_issues": self._check_grammar(text),
        }

    def _extract_themes(self, text: str) -> List[str]:
        """Extract potential themes using keyword frequency"""
        words = re.findall(r"\b\w+\b", text.lower())
        # Remove common stop words
        stop_words = {
            "the",
            "a",
            "an",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "for",
            "of",
            "with",
            "by",
            "is",
            "are",
            "was",
            "were",
            "be",
            "been",
            "being",
            "have",
            "has",
            "had",
            "do",
            "does",
            "did",
            "will",
            "would",
            "could",
            "should",
            "may",
            "might",
            "must",
            "can",
            "shall",
        }
        filtered_words = [
            word for word in words if word not in stop_words and len(word) > 3
        ]
        word_counts = Counter(filtered_words)
        # Return top 10 most common words as themes
        return [word for word, _ in word_counts.most_common(10)]

    def _analyze_discourse(self, text: str) -> Dict[str, Any]:
        """Analyze discourse patterns"""
        sentences = re.split(r"[.!?]+", text)
        sentences = [s.strip() for s in sentences if s.strip()]

        questions = len([s for s in sentences if s.endswith("?")])
        exclamations = len([s for s in sentences if s.endswith("!")])

        return {
            "sentence_count": len(sentences),
            "question_count": questions,
            "exclamation_count": exclamations,
            "average_sentence_length": sum(len(s.split()) for s in sentences)
            / len(sentences)
            if sentences
            else 0,
        }

    def _analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """Basic sentiment analysis using word lists"""
        words = re.findall(r"\b\w+\b", text.lower())
        positive_count = sum(1 for word in words if word in self.POSITIVE_WORDS)
        negative_count = sum(1 for word in words if word in self.NEGATIVE_WORDS)

        total_words = len(words)
        sentiment_score = (
            (positive_count - negative_count) / total_words if total_words > 0 else 0
        )

        return {
            "positive_words": positive_count,
            "negative_words": negative_count,
            "sentiment_score": sentiment_score,  # -1 to 1
            "sentiment": "positive"
            if sentiment_score > 0.1
            else "negative"
            if sentiment_score < -0.1
            else "neutral",
        }

    def _analyze_linguistics(self, text: str) -> Dict[str, Any]:
        """Analyze linguistic features"""
        words = re.findall(r"\b\w+\b", text)
        sentences = re.split(r"[.!?]+", text)
        sentences = [s.strip() for s in sentences if s.strip()]

        total_words = len(words)
        unique_words = len(set(word.lower() for word in words))
        avg_word_length = (
            sum(len(word) for word in words) / total_words if total_words > 0 else 0
        )

        return {
            "word_count": total_words,
            "unique_words": unique_words,
            "sentence_count": len(sentences),
            "average_word_length": avg_word_length,
            "lexical_diversity": unique_words / total_words if total_words > 0 else 0,
        }

    def _analyze_readability(self, text: str) -> Dict[str, Any]:
        """Calculate basic readability metrics"""
        words = re.findall(r"\b\w+\b", text)
        sentences = re.split(r"[.!?]+", text)
        sentences = [s.strip() for s in sentences if s.strip()]

        total_words = len(words)
        total_sentences = len(sentences)
        total_syllables = sum(self._count_syllables(word) for word in words)

        # Flesch Reading Ease
        if total_sentences > 0 and total_words > 0:
            flesch_score = (
                206.835
                - 1.015 * (total_words / total_sentences)
                - 84.6 * (total_syllables / total_words)
            )
        else:
            flesch_score = 0

        return {
            "flesch_reading_ease": flesch_score,
            "grade_level": self._flesch_to_grade(flesch_score),
            "words_per_sentence": total_words / total_sentences
            if total_sentences > 0
            else 0,
            "syllables_per_word": total_syllables / total_words
            if total_words > 0
            else 0,
        }

    def _analyze_quality(self, text: str) -> Dict[str, Any]:
        """Analyze writing quality indicators"""
        words = re.findall(r"\b\w+\b", text)
        sentences = re.split(r"[.!?]+", text)
        sentences = [s.strip() for s in sentences if s.strip()]

        total_words = len(words)
        total_sentences = len(sentences)

        avg_sentence_length = (
            total_words / total_sentences if total_sentences > 0 else 0
        )

        # Simple quality metrics
        long_sentences = sum(1 for s in sentences if len(s.split()) > 25)
        short_sentences = sum(1 for s in sentences if len(s.split()) < 5)

        return {
            "average_sentence_length": avg_sentence_length,
            "long_sentences": long_sentences,
            "short_sentences": short_sentences,
            "sentence_variety": (long_sentences + short_sentences) / total_sentences
            if total_sentences > 0
            else 0,
        }

    def _analyze_vocabulary(self, text: str) -> Dict[str, Any]:
        """Analyze vocabulary richness"""
        words = re.findall(r"\b\w+\b", text.lower())
        total_words = len(words)
        unique_words = len(set(words))

        # Hapax legomena (words appearing once)
        word_counts = Counter(words)
        hapax = sum(1 for count in word_counts.values() if count == 1)

        return {
            "total_words": total_words,
            "unique_words": unique_words,
            "vocabulary_richness": unique_words / total_words if total_words > 0 else 0,
            "hapax_legomena": hapax,
            "hapax_percentage": hapax / total_words if total_words > 0 else 0,
        }

    def _check_grammar(self, text: str) -> List[str]:
        """Basic grammar and style checks"""
        issues = []

        # Check for double spaces
        if "  " in text:
            issues.append("Contains double spaces")

        # Check for multiple consecutive punctuation
        if re.search(r"[.!?]{2,}", text):
            issues.append("Multiple consecutive punctuation marks")

        # Check for sentences starting with lowercase
        sentences = re.split(r"[.!?]+", text)
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence and sentence[0].islower():
                issues.append("Sentence starts with lowercase letter")
                break  # Only report once

        # Check for missing spaces after punctuation
        if re.search(r"[.!?][A-Z]", text):
            issues.append("Missing space after punctuation")

        return issues

    def _count_syllables(self, word: str) -> int:
        """Count syllables in a word (basic implementation)"""
        word = word.lower()
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count += 1
        return count

    def _flesch_to_grade(self, score: float) -> str:
        """Convert Flesch score to grade level"""
        if score >= 90:
            return "5th grade"
        elif score >= 80:
            return "6th grade"
        elif score >= 70:
            return "7th grade"
        elif score >= 60:
            return "8th-9th grade"
        elif score >= 50:
            return "10th-12th grade"
        elif score >= 30:
            return "College"
        else:
            return "College Graduate"
