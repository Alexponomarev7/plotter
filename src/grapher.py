# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

import tkinter
import math
from point import point
from drawing import draw

MAX_WIDTHSIZE = 1485     # 210 mm
MAX_HEIGHTSIZE = 1050    # 297 mm
PRECISION = 10

# Parsing function
def func(x, function):
    function.replace('x', str(x))
    return eval(function)

# Creating graphic
def create_graphic(function, x_pos, y_pos, SCALE, path):
    graphic = []
    for i in range(-250 * PRECISION, 250 * PRECISION + 1):
        j = i / PRECISION
        try:
            p = point(j * SCALE + MAX_WIDTHSIZE / 2,
                      -func(j, function) * SCALE + MAX_HEIGHTSIZE / 2)
            graphic.append(p)
        except ZeroDivisionError:
            continue
 
    draw(graphic, path, "graphic", SCALE)


# Creating GUI
def main(path, function, x_pos, y_pos, SCALE):    
    graphic = []
    create_graphic(function, x_pos, y_pos, SCALE, path)    