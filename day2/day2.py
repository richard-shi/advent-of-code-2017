#!/usr/bin/env python3

#!/usr/bin/env python3

"""
Solution to Advent of Code 2017 Day 2 problems
"""

INPUT_FILE = 'day2/input'

def diff_test():
    """Tests for diff"""
    assert diff([5, 1, 9, 5]) == 8
    assert diff([7, 5, 3]) == 4
    assert diff([2, 4, 6, 8]) == 6

def evenly_divisible_test():
    """Tests for evenly_divisible"""
    assert evenly_divisible([5, 9, 2, 8]) == 4
    assert evenly_divisible([9, 4, 7, 3]) == 3
    assert evenly_divisible([3, 8, 6, 5]) == 2

def evenly_divisible(row):
    """ Find the product of the only two evenly divisible numbers """
    for num in row:
        for other_num in row:
            if num != other_num and (num / other_num).is_integer():
                return num / other_num


def diff(row):
    """Return difference between highest and lowest numbers in row"""
    return max(row) - min(row)

def checksum():
    """ Get Checksum """

    with open(INPUT_FILE) as input_file:
        checksum = 0
        for line in input_file:
            row = list(map(int, line.split()))
            checksum += evenly_divisible(row)
        return checksum

def main():
    """Main function"""
    print(checksum())


if __name__ == '__main__':
    main()
