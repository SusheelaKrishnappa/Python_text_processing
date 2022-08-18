import src.WordFrequencyAnalyser.WordFrequencyAnalyzer as wfa
import pytest

from test.inputs import data1,data2


# TEST 1 - HIGHEST FREQUENCY
def test_calculate_highest_frequency(input_value):
    obj = wfa.WordFrequencyAnalyzer()
    res = obj.calculate_highest_frequency(input_value)
    assert res[1] == 2


@pytest.mark.parametrize(
    "test_input,expected",
    [(data1, 2), (data2, 2),
     pytest.param("", 42, marks=pytest.mark.xfail())]
)
def test_to_calculate_highest_frequency(test_input, expected):
    obj = wfa.WordFrequencyAnalyzer()
    res = obj.calculate_highest_frequency(test_input)
    assert res[1] == expected


# TEST 2 - FREQUENCY for specific word
def test_calculate_frequency_for_word(input_value):
    text_to_search = "the"
    obj = wfa.WordFrequencyAnalyzer()
    res = obj.calculate_frequency_for_word(input_value, text_to_search)
    assert res == 2


@pytest.mark.parametrize(
    "test_input,expected",
    [(data1, 2), (data2, 2),
     pytest.param("", 42, marks=pytest.mark.xfail())]
)
def test_to_calculate_frequency_for_word(test_input, expected):
    text_to_search = "the"
    obj = wfa.WordFrequencyAnalyzer()
    res = obj.calculate_frequency_for_word(test_input, text_to_search)
    assert res == expected


# TEST 3 - FREQUENCY for n words
def test_calculate_most_frequent_n_words(input_value):
    n = 3
    obj = wfa.WordFrequencyAnalyzer()
    res = obj.calculate_most_frequent_n_words(input_value, n)
    assert len(res) == 3


@pytest.mark.parametrize(
    "test_input,expected",
    [(data1, 3), (data2, 3),
     pytest.param("", 42, marks=pytest.mark.xfail())]
)
def test_to_calculate_most_frequent_n_words(test_input, expected):
    n = 3
    obj = wfa.WordFrequencyAnalyzer()
    res = obj.calculate_most_frequent_n_words(test_input, n)
    assert len(res) == expected
