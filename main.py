"""This is the main file for text processing"""
import src.WordFrequencyAnalyser.WordFrequencyAnalyzer as wfa

# Main
if __name__ == '__main__':
    while (True):
        print("Please select the options")
        choices = ["Enter 1 for calculating highest frequency", "Enter 2 for calculating frequency for "
                                                                "specific word", "Enter 3 for calculates "
                                                                                 "the most frequency of n "
                                                                                 "words"]
        for k in choices:
            print(k)

        try:
            choice = int(input())
        except ValueError:
            print("That was not valid number, try again...")
            continue
        if choice == 1:
            text = input("Enter the text for processing \t")
            obj = wfa.WordFrequencyAnalyzer()
            t, f = obj.calculate_highest_frequency(text)
            print("The highest frequency of the word in \"{}\" is {}".format(t, f))

        elif choice == 2:
            text = input("Enter the text for processing \t")
            word = input("Enter text for finding its frequency \t")
            obj = wfa.WordFrequencyAnalyzer()
            f = obj.calculate_frequency_for_word(text, word)
            print("The frequency of \"{}\" in text is {}  :".format(word, f))

        elif choice == 3:
            text = input("Enter the text for processing \t")
            n = int(input("Enter the list n words to returned \t"))
            obj = wfa.WordFrequencyAnalyzer()
            word_freq_list = obj.calculate_most_frequent_n_words(text, n)
            print("List of word frequencies: {}".format(word_freq_list))

        else:
            print("Entered wrong choice, Please try again...")
