"""This module contains the Word Frequency and WordFrequencyAnalyser"""
from typing import List
import re

from src.utils.utils import cal_frequency


class WordFrequency:
    """"Class uses the word to calculate its frequency
    Attributes
    ---------
    word: str
    a word is sequence of one or more characters between a nd z or between A and Z
    frequency: int
    number of occurrences in the given string
    """

    def __init__(self, word: str, frequency: int):
        """"Constructor which initializes word and frequency
        Attributes
        ---------
        word: str
        a word is sequence of one or more characters between a nd z or between A and Z
        frequency: int
        number of occurrences in the given string
        """
        # Validate the instance variable
        self.__word, self.__frequency = self.validator(word, frequency)

    @property
    def word(self) -> str:
        """str: word of the instance referenced by self"""
        return self.__word

    @property
    def frequency(self) -> int:
        """int: frequency of the instance referenced by self"""
        return self.__frequency

    def validator(self, word: str, frequency: int):
        """This method validates word and frequency inputs
        :parameter
        word: str
        frequency: int
        :return
        word: str
        frequency: int
        """
        if not isinstance(word, str):
            raise TypeError("word: should be string")
        if re.search("[@_!#$%^&*()<>?/|}{~:]", word):
            raise ValueError("word cannot contain special characters")

        if not isinstance(frequency, int):
            raise TypeError("frequency type should be integer")
        return word, frequency


class WordFrequencyAnalyzer():
    """This class implements text processing operations like calculating highest frequency"""

    def calculate_highest_frequency(self, text: str) -> int:
        """This method calculates takes input text, returns the highest frequency of the word in
        the text
        :parameter
        text: str
        input string contains various words
        :return
        highest frequency of the word in the text
        """
        text = cal_frequency.data_validator(text)
        highest_freq = cal_frequency.calculate_frequency(text)[0][1]
        return cal_frequency.calculate_frequency(text)[0][0], highest_freq

    def calculate_frequency_for_word(self, text: str, word: str) -> int:
        """This method calculates frequency for specific word, returns the computed frequency
        :parameter
        text: str
            input string contains various words
        word: str
            sequence of characters between [a-z] or [A-Z]
        :return
        frequency of given word
        """
        text = cal_frequency.data_validator(text)
        count = 0
        word_list = text.split(" ")
        for wrd in word_list:
            if re.search(wrd, word, re.IGNORECASE):
                count += 1
        return count

    def calculate_most_frequent_n_words(self, text: str, n: int) -> List:
        """This method calculates the most frequency of n words,returns tuple in alphabetical order
        :parameter
        text: str
        n: int
            number of most common words
        :returns
        list of tuples in (word,frequency)

        """

        text = cal_frequency.data_validator(text)
        result = cal_frequency.calculate_n_frequency(text, n)
        # List of Wordfrequency
        word_freq_list = [(WordFrequency.word, WordFrequency.frequency)]
        word_freq_list.clear()

        for i in range(0, len(result)):
            word_freq_list.append(result[i])
        return word_freq_list
