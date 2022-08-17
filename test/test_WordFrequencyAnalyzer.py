import src.WordFrequencyAnalyser.WordFrequencyAnalyzer as wfa
import pytest


# TEST 1 - HIGHEST FREQUENCY
def test_calculate_highest_frequency(input_value):
    obj = wfa.WordFrequencyAnalyzer()
    res = obj.calculate_highest_frequency(input_value)
    print(input_value)
    print("Highest frequency of the word : {} is {}".format(res[0], res[1]))
    assert res[1] == 2


@pytest.mark.parametrize(
    "test_input,expected",
    [("the sun shines over the lake", 2), ("@#$$$the#$$&sun$$shines_)[[]]($over%%the@@lake", 2),
     pytest.param("", 42, marks=pytest.mark.xfail())]
)
def test_to_calculate_highest_frequency(test_input, expected):
    obj = wfa.WordFrequencyAnalyzer()
    res = obj.calculate_highest_frequency(test_input)
    print("Highest frequency of the word : {} is {}".format(res[0], res[1]))
    assert res[1] == expected


# TEST 2 - FREQUENCY for specific word
def test_calculate_frequency_for_word(input_value):
    text_to_search = "the"
    obj = wfa.WordFrequencyAnalyzer()
    res = obj.calculate_frequency_for_word(input_value, text_to_search)
    assert res == 2


@pytest.mark.parametrize(
    "test_input,expected",
    [("the sun shines over the lake", 2), ("@#$$$the#$$&sun$$shines_)[[]]($over%%the@@lake", 2),
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
    print(res)


@pytest.mark.parametrize(
    "test_input,expected",
    [("the sun shines over the lake", 3), ("@#$$$the#$$&sun$$shines_)[[]]($over%%the@@lake", 3),
     pytest.param("", 42, marks=pytest.mark.xfail())]
)
def test_to_calculate_most_frequent_n_words(test_input, expected):
    n = 3
    obj = wfa.WordFrequencyAnalyzer()
    res = obj.calculate_most_frequent_n_words(test_input, n)
    assert len(res) == expected


@pytest.mark.parametrize(
    "text_processing_input,expected",
    [("the sun shines over the lake", 3), ("@#$$$the#$$&sun$$shines_)[[]]($over%%the@@lake", 3),
     pytest.param("", 42, marks=pytest.mark.xfail())]
)
def test_to_calculate_most_frequent_n_words(text_processing_input, expected):
    n = 3
    obj = wfa.WordFrequencyAnalyzer()
    res = obj.calculate_most_frequent_n_words(text_processing_input, n)
    assert len(res) == expected
