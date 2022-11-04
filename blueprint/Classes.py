from dataclasses import dataclass
from enum import Enum


class Moves(Enum):
    """
    Enum object for the possible moves in the map array
    """
    NONE = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


@dataclass
class Puzzle:
    """
    Object, which stores:
    The current Moves(Enum) object -> think of it like an integer but instead of numbers 0,1,2,3
    there are NONE, LEFT, RIGHT ...
    The map array: e.g. [[3,4,5],
                         [0,2,6],
                         [7,8,1]
                        ]
    The previous puzzle object, which helps in reproducing the steps taken from first to last for the GUI part
    """
    move: Moves
    map: list[list[int]]
    prev_puzzle: None
