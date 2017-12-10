#!/usr/bin/env python3

"""
Solution to Advent of Code 2017 Day 5 problems
"""

INPUT_FILE = 'day5/input'

def test_traverse():
    assert traverse([0, 3, 0, 1, -3]) == 5

def load_jump_list():
    jump_list = []
    with open(INPUT_FILE) as input_file:
        for line in input_file:
            jump_list.append(int(line))
        return jump_list

def traverse(jump_list):
    steps = 0
    iptr = 0
    while 0 <= iptr and iptr < len(jump_list):
        offset = jump_list[iptr]
        jump_list[iptr] += 1
        iptr += offset
        steps += 1
    return steps

def main():
    """Main function"""
    test_traverse()

    jump_list = load_jump_list()
    steps = traverse(jump_list)
    print(steps)

if __name__ == '__main__':
    main()
