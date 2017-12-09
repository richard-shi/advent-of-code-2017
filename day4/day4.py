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

def main():
    """Main function"""
    with open(INPUT_FILE) as input_file:
        amount = 0
        for line in input_file:
            amount += 1 if unique_words(line) else 0
        print(amount)

if __name__ == '__main__':
    main()
