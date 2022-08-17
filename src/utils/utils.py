"""This is the util for calculating frequencies"""
from collections import Counter
from typing import List


class cal_frequency:
    """This class performs frequency calculation operations"""
    def calculate_frequency(text: str) -> List:
        """This method calculates frequency of the word
        :parameter
        text: str
         contains many words
        :return
        highest frequency
        """
        word_list = text.split(" ")
        counter = Counter(word_list)
        return counter.most_common()

    def calculate_n_frequency(text: str, n: int) -> List:
        """This method calculates frequency of the word
                :parameter
                text: str
                 contains many words
                n: int
                number of common words
                :return
                highest frequency
                """
        word_list = text.split(" ")
        counter = Counter(sorted(word_list)).most_common(n)
        return counter
