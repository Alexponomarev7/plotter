# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

import tkinter
from math import sqrt, sin, cos
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
def create_graphic(function, x_pos, y_pos, SCALE, path):
    graphic = []
    min_x = int(-(WIDTH / (2 * SCALE)) - 1)
    max_x = int(WIDTH / (2 * SCALE) + 1)
    for i in range(min_x * PRECISION, max_x * PRECISION + 1):
        j = i / PRECISION
        try:
            p = point(j * SCALE + WIDTH / 2,
                -func(j, function) * SCALE + HEIGHT / 2)
            graphic.append(p)
        except NameError:
            raise
        except:
            print(traceback.format_exc(), file=sys.stderr)
            continue
 
    draw(graphic, path, "graphic", SCALE)


# Creating GUI
def main(path, function, x_pos, y_pos, SCALE):
    global PRECISION
    PRECISION = int(SCALE // 10)
    
    graphic = []
    create_graphic(function, x_pos, y_pos, SCALE, path)    