import pytest
from src.WordFrequencyAnalyser import WordFrequencyAnalyzer
from src.WordFrequencyAnalyser.WordFrequencyAnalyzer import WordFrequency

@pytest.fixture
def input_value():
    word = "the sun shines over the lake"
    frequency = 0
    try:
        word_frequency = WordFrequency(word, frequency)
        return word_frequency.word
    except (ValueError, TypeError) as er:
        return str(er)








