#!/usr/bin/env python3

"""
Solution to Advent of Code 2017 Day 1 problem part 1
"""

INPUT_FILE = 'day1/input'

def test_captcha():
    assert captcha([1, 1, 2, 2]) == 3
    assert captcha([1, 1, 1, 1]) == 4
    assert captcha([1, 2, 3, 4]) == 0
    assert captcha([9, 1, 2, 1, 2, 1, 2, 9]) == 9
    
def captcha(digits):
    """Sum digits that are with the ones beside it"""
    digit_sum = 0
    for index, digit in enumerate(digits):
        if index < len(digits) - 1 and digit == digits[index + 1]:
            digit_sum += int(digit)
        elif index == len(digits) - 1 and digit == digits[0]:
            digit_sum += int(digit)
    return digit_sum

if __name__ == '__main__':
    # test_captcha()

    with open(INPUT_FILE) as input_file:
        digit_list = list(input_file.read()) # Might as well do one big read
        digit_sum = captcha(digit_list)
        print(digit_sum)
