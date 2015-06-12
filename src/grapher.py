# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

import tkinter
import math 
from point import point
from drawing import draw

MAX_WIDTHSIZE = 500     #210 mm
MAX_HEIGHTSIZE = 500    #297 mm
SCALE = 71
PRECISION = 10

def increase():
    global SCALE
    SCALE += 10

def degrease():
    global SCALE
    SCALE = max(1, SCALE - 10)

#increasing scale
def plus(event):
    #some code, which cleaning Canvas
    panel.delete("group")
    increase()
    create_graphic(panel, function)

#degreasing scale
def minus(event):
    #some code, which cleaning Canvas
    panel.delete("group")
    degrease()
    create_graphic(panel, function)

#parsing function
def func(x, function):
    function.replace('x', str(x))
    return eval(function)

#drawing graphic
def draw_graphic(p, panel):
    for i in range(len(p) - 1):
        panel.create_line(p[i].x + MAX_WIDTHSIZE / 2,
                          p[i].y + MAX_HEIGHTSIZE / 2,
                          p[i + 1].x + MAX_WIDTHSIZE / 2,
                          p[i + 1].y + MAX_HEIGHTSIZE / 2,
                          fill="red", tag="group")
        
    draw(p, "graphic")
    

#creating graphic
def create_graphic(panel, function):
    graphic = []
    for i in range(-250 * PRECISION, 250 * PRECISION + 1):
        j = i / PRECISION
        try:
            p = point(j * SCALE, -func(j, function) * SCALE)
            graphic.append(p)
        except ZeroDivisionError:
            continue
            
    draw_graphic(graphic, panel)

#creating GUI
root = tkinter.Tk()
panel = tkinter.Canvas(root, width=MAX_WIDTHSIZE, height=MAX_HEIGHTSIZE)
panel.grid(row=0, column=0)

graphic = []
function = input('y = ')
panel.create_line(MAX_WIDTHSIZE / 2, 0, MAX_WIDTHSIZE / 2, MAX_HEIGHTSIZE,
                  fill="gray50")
panel.create_line(0, MAX_HEIGHTSIZE / 2, MAX_WIDTHSIZE, MAX_HEIGHTSIZE / 2,
                  fill="gray50")
create_graphic(panel, function)

root.bind('<i>', plus)   #increase
root.bind('<d>', minus)  #degrease
root.mainloop()