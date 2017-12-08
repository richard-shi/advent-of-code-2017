#!/usr/bin/env python3

"""
Solution to Advent of Code 2017 Day 1 problem part 1
"""

INPUT_FILE = 'day1/input'

def part1_test():
    """Part 1 tests"""
    assert part1([1, 1, 2, 2]) == 3
    assert part1([1, 1, 1, 1]) == 4
    assert part1([1, 2, 3, 4]) == 0
    assert part1([9, 1, 2, 1, 2, 1, 2, 9]) == 9

def part1(digits):
    """Sum digits that are with the ones beside it"""
    digit_sum = 0
    for index, digit in enumerate(digits):
        if index < len(digits) - 1 and digit == digits[index + 1]:
            digit_sum += int(digit)
        elif index == len(digits) - 1 and digit == digits[0]:
            digit_sum += int(digit)
    return digit_sum

# def part2(digits):
#     """Sum digits that are with the ones beside it"""
#     digit_sum = 0
#     for index, digit in enumerate(digits):
#         if index < len(digits) - 1 and digit == digits[index + 1]:
#             digit_sum += int(digit)
#         elif index == len(digits) - 1 and digit == digits[0]:
#             digit_sum += int(digit)
#     return digit_sum

def main():
    """Main function"""
    with open(INPUT_FILE) as input_file:
        input_data = list(input_file.read()) # Might as well do one big read
        result = part1(input_data)
        print(result)

if __name__ == '__main__':
    main()
