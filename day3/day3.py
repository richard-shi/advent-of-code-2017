#!/usr/bin/env python3

"""
Solution to Advent of Code 2017 Day 3 problems
"""
from math import sqrt, floor

def closest_odd(number):
    """Returns number if odd, else returns next number below"""
    return number if number % 2 == 1 else number - 1

def largest_square_under(number):
    """Returns largest square value under `number`"""
    return floor(sqrt(number))

def ring_num(number):
    odd_sq = closest_odd(largest_square_under(number))
    return (odd_sq + 1) // 2 if odd_sq ** 2 >= number else (odd_sq + 1) // 2 + 1

def bottom_right_corner(number):
    """Returns which ring a number is in"""
    return (ring_num(number) * 2 - 1) ** 2


def manhattan_dist(number):
    """ Finds Manhattan distance between `number` and 1 in the
        grid center.
    """
    return abs(number - bottom_right_corner(number))

def main():
    """Main function"""

if __name__ == '__main__':
    main()
