import operator
import re
from typing import List


def top_three_used_words(text: str) -> List[str]:
    # split text by commas and spaces
    splitted_text = re.split(',| ', text.lower())

    # get clean words from splitted text
    clean_words = []
    for dirty_word in splitted_text:
        # returns matching to pattern "letters a-z with '" strings
        subwords = re.findall("[a-z']+", dirty_word)

        # if word hasn't got special characters inside (allows left and right sides of the word)
        if len(subwords) == 1:
            clean_words.append(subwords[0])

    # count words
    words_and_repetitions = {}
    for word in clean_words:
        if word not in words_and_repetitions.keys():
            repetitions = clean_words.count(word)
            words_and_repetitions[word] = repetitions

    # sort by desc
    sorted_words = dict(sorted(words_and_repetitions.items(), key=operator.itemgetter(1), reverse=True))

    if len(sorted_words.keys()) < 3:
        return []

    return list(sorted_words.keys())[0:3]
