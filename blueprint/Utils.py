import random
from copy import deepcopy
from Classes import *


def print_map(puzzle):
    map_array = deepcopy(puzzle.map)
    print()
    for i in range(len(map_array)):
        print(map_array[i])
    print()


def create_array(puzzle: Puzzle):
    array = []
    while puzzle.prev_puzzle is not None:
        array.insert(0, puzzle)
        puzzle = puzzle.prev_puzzle
    array.insert(0, puzzle)
    return array
