#!/usr/bin/env python3

"""
Solution to Advent of Code 2017 Day 4 problems
"""

INPUT_FILE = 'day4/input'

def unique_words_test():
    """Tests for unique_words"""
    assert unique_words('aa bb cc dd ee')
    assert not unique_words('aa bb cc dd aa')
    assert unique_words('aa bb cc dd aaa')

def unique_words(phrase):
    """ Returns if a phrase has only unique words """
    used_words = set()

    words = phrase.split()
    for word in words:
        if word in used_words:
            return False
        used_words.add(word)

    return True

def is_anagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)

def no_anagrams(phrase):
    """ Returns if a phrase has no anagrams """
    used_words = []

    words = phrase.split()
    for word in words:
        for old_word in used_words: 
            if is_anagram(old_word, word):
                return False
        used_words.append(word)

    return True

def main():
    """Main function"""

    with open(INPUT_FILE) as input_file:
        amount = 0
        for line in input_file:
            amount += 1 if no_anagrams(line) else 0
        print(amount)

if __name__ == '__main__':
    main()
