import pytest
from src.WordFrequencyAnalyser import WordFrequencyAnalyzer
from src.WordFrequencyAnalyser.WordFrequencyAnalyzer import WordFrequency
from test.inputs import data1

@pytest.fixture
def input_value():
    word = data1
    frequency = 0
    try:
        word_frequency = WordFrequency(word, frequency)
        return word_frequency.word
    except (ValueError, TypeError) as er:
        return str(er)
