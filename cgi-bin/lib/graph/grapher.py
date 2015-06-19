# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

import tkinter
from math import sqrt, sin, cos, pi
from math import tan as tg
from .point import point
from .drawing import draw
from .. import const
import sys, traceback

CHECK = 10000      # Checking for discontinue
WIDTH = const.X_REAL_RESOLUTION * const.PIXELS_PER_MM   # 210 mm
HEIGHT = const.Y_REAL_RESOLUTION * const.PIXELS_PER_MM  # 297 mm
PRECISION = 10

f = []

def func_decorator(function):
    def func_inner(x):
        return func(x, function)
    return func_inner

# Parsing function
def func(x, function):
    return eval(function)

def ctg(x):
    return 1 / tg(x)

# Creating graphic
def create_graphic(function, x_pos, y_pos, SCALE, name):
    graphic = []
    min_x = -(WIDTH / (2 * SCALE))
    max_x = WIDTH / (2 * SCALE)
    dx = 1 / PRECISION
    last = 0
    while min_x <= max_x:
        min_x += dx        
        try:
            new_y = -func(min_x, function)
            if type(new_y) is complex:
                continue
            p = point(min_x * SCALE + WIDTH / 2,
                new_y * SCALE + HEIGHT / 2)
            if abs(last - new_y) / dx >= CHECK:
                graphic.append(None)
            last = new_y
            graphic.append(p)
        except NameError:
            raise
        except:
            continue

    return graphic
#    draw(graphic, name, "graphic", SCALE)


# Creating GUI
def main(name, function_list, x_pos, y_pos, SCALE):
    global PRECISION
    PRECISION = int(SCALE) * const.PRECISION_MULTIPLIER
    
    graphic = []

    f[:] = [func_decorator(function[0]) for function in function_list]
    for function in function_list:
        if function[1]:
            points = create_graphic(function[0], x_pos, y_pos, SCALE, name)    
            graphic += [None]
            graphic += points

    aux_task = draw(graphic, name, "graphic", SCALE)
    return (aux_task, graphic)
