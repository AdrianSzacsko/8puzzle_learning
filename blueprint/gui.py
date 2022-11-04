import time
import tkinter
from tkinter import ALL

from Classes import *
import random

array_for_colors = []
array_for_colornames = []


def create_map(window, offset_x, offset_y, rectangle_size):
    for i in range(0, rectangle_size*3, rectangle_size):
        for j in range(0, rectangle_size*3, rectangle_size):
            window.create_rectangle(offset_y + i, offset_x + j, offset_y + i + rectangle_size, offset_x + j +
                                    rectangle_size, dash=(3, 5), fill="White")


def draw_number(window, map_array, offset_x, offset_y, rectangle_size):
    for i in range(0, 3):
        for j in range(0, 3):
            if map_array[i][j] != 0:
                window.create_text(offset_y + j * rectangle_size + rectangle_size/2, offset_x + i * rectangle_size +
                                   rectangle_size/2, text=str(map_array[i][j]), font="Times 20")


def create_gui_table(window, offset_x, offset_y, rectangle_size, array):
    create_map(window, offset_x, offset_y, rectangle_size)
    draw_number(window, array, offset_x, offset_y, rectangle_size)


def create_text(window, offset_x, offset_y, rectangle_size, array, i):
    if i >= len(array):
        i = len(array) - 1
    return window.create_text(offset_y, offset_x + 7 * rectangle_size, text=str(i+1)+": "+array[i], anchor=tkinter.SW,
                              font=("Arial", 34))


# create steps from first to last
def gui_array(array, window):
    #text = ""
    time.sleep(3)
    for i in range(len(array)):
        time.sleep(0.4)
        window.update()
        window.delete(ALL)
        #window.itemconfig(text, text="")
        create_gui_table(window, 50, 50, 100, array[i].map)
        #text = create_text(window, offset_x, offset_y, rectangle_size, array, i)


# create one step and draw it
def gui_step(puzzle, window):
    window.update()
    window.delete(ALL)
    #window.itemconfig(text, text="")
    create_gui_table(window, 50, 50, 100, puzzle.map)
