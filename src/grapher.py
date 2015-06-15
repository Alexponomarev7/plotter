# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

import tkinter
import math
from point import point
from drawing import draw

MAX_WIDTHSIZE = 500     # 210 mm
MAX_HEIGHTSIZE = 500    # 297 mm
SCALE = 71
PRECISION = 10
path = None

def increase():
    global SCALE
    SCALE += 10


def decrease():
    global SCALE
    SCALE = max(1, SCALE - 10)


# Increasing scale
def plus(event):
    # Some code, which cleaning Canvas
    panel.delete("group")
    increase()
    create_graphic(panel, function)


# Decreasing scale
def minus(event):
    # Some code, which cleaning Canvas
    panel.delete("group")
    decrease()
    create_graphic(panel, function)


# Parsing function
def func(x, function):
    function.replace('x', str(x))
    return eval(function)


# Drawing graphic
def draw_graphic(p, panel):
    global path
    
    # for i in range(len(p) - 1):
    #    panel.create_line(p[i].x, p[i].y, p[i + 1].x, p[i + 1].y,
    #                      fill="red", tag="group")

    draw(p, path)


# Creating graphic
def create_graphic(panel, function):
    graphic = []
    for i in range(-250 * PRECISION, 250 * PRECISION + 1):
        j = i / PRECISION
        try:
            p = point(j * SCALE + MAX_WIDTHSIZE / 2,
                      -func(j, function) * SCALE + MAX_HEIGHTSIZE / 2)
            graphic.append(p)
        except ZeroDivisionError:
            continue
 
    draw_graphic(graphic, panel)


# Creating GUI
def main(name, function):
    global path
    path = name
    
    # root = tkinter.Tk()
    # panel = tkinter.Canvas(root, width=MAX_WIDTHSIZE, height=MAX_HEIGHTSIZE)
    # panel.grid(row=0, column=0)
    
    graphic = []
    # panel.create_line(MAX_WIDTHSIZE / 2, 0, MAX_WIDTHSIZE / 2, MAX_HEIGHTSIZE,
    #                  fill="gray50")
    # panel.create_line(0, MAX_HEIGHTSIZE / 2, MAX_WIDTHSIZE, MAX_HEIGHTSIZE / 2,
    #                  fill="gray50")
    panel = None
    create_graphic(panel, function)
    
    # root.bind('<i>', plus)   # Increase
    # root.bind('<d>', minus)  # decrease
    # root.mainloop()
