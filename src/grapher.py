# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

import tkinter
from math import sqrt, sin, cos, pi
from math import tan as tg
from point import point
from drawing import draw
import sys, traceback

WIDTH = 1485     # 210 mm
HEIGHT = 1050    # 297 mm
PRECISION = 10

# Parsing function
def func(x, function):
    return eval(function)

# Creating graphic
def create_graphic(function, x_pos, y_pos, SCALE, name):
    graphic = []
    min_x = int(-(WIDTH / (2 * SCALE)) - 1)
    max_x = int(WIDTH / (2 * SCALE) + 1)
    dx = 1 / PRECISION
    last = 0
    for i in range(min_x * PRECISION, max_x * PRECISION + 1):
        j = i / PRECISION
        try:
            new_y = -func(j, function)
            p = point(j * SCALE + WIDTH / 2,
                new_y * SCALE + HEIGHT / 2)
            if abs(last - new_y) / dx >= 10 ** 2:
                graphic.append(None)
            last = new_y
            graphic.append(p)
        except NameError:
            raise
        except:
            print(traceback.format_exc(), file=sys.stderr)
            continue
 
    draw(graphic, name, "graphic", SCALE)


# Creating GUI
def main(name, function, x_pos, y_pos, SCALE):
    global PRECISION
    PRECISION = int(SCALE // 10)
    
    graphic = []
    create_graphic(function, x_pos, y_pos, SCALE, name)    