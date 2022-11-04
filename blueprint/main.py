import sys
import time
import tkinter

import gui
from Classes import *
from Utils import *


def load_file(path: str):
    """
        This function need to read a file and create a 2D array of numbers
        The numbers need to be positioned as in the file e.g. [[3,4,5],
                                                               [0,2,6],
                                                               [7,8,1]
                                                              ]
        :param path: the path to the file
        :return Puzzle:
    """


def move(puzzle: Puzzle, position):
    """
    This function generates new moves (swaps numbers in the map array). It reads the 'move' variable from the puzzle
    object and according to the variable swaps the numbers in the array and then returns the puzzle object
    :param puzzle: Puzzle object
    :param position: The indexes (x,y) in the map array, where the 0 is located
    :return: Puzzle object
    """


def solve_bfs(puzzle: Puzzle, container: list, window):
    """
    main function for the program to funtion. It processes the puzzles and generates new ones, checks whether the new
    puzzles are solved
    :param puzzle: First puzzle object with the original positions read from a file
    :param container: The data structure (queue or stack), where the unprocessed, but generated puzzles are stored. Only
    puzzles which were not yet processed and checked are stored here
    :param window: object to create the gui element, not mandatory to use
    :return: returns the solved puzzle from which the steps will be created
    """
    ### add puzzle to the container, use deepcopy()

    ### add puzzle to set (it is like an array but hashed) -> puzzle object need to be converted to string before adding
    ### it to set

    #start = time.time()
    ### create new maps until it is solved (need a loop) or container is empty

        #sys.stdout.write(
        #    "\rUnprocessed nodes: " + str(len(container)) + "\tProcessed nodes: " + str(len(sets)) +
        #    "\tElapsed time: {:.2f}s".format(time.time() - start))
        ### to process a puzzle, we need to take it out from container, use deepcopy

        # gui.gui_step(puzzle, window)
        ### check if we have solved the map


        ### create new nodes - check moves, create new puzzle objects according to new moves and if not in set,
        ### add to container

    ### map can not be solved

### Do not edit below these lines-------------------------------------------------------------------------------
def main():
    window = tkinter.Canvas(width=400, height=400)
    window.pack()
    # we need to load from a file
    # path = input("Add puzzle: ")
    path = "map.txt"
    file_puzzle = load_file("maps//" + path)
    solved_puzzle = solve-_bfs(file_puzzle, [], window)
    print_map(solved_puzzle)
    # create gui_array
    steps = create_array(solved_puzzle)
    print("Step count:", len(steps))
    gui.gui_array(steps, window)
    window.mainloop()


if __name__ == "__main__":
    main()
