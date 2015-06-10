# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

import tkinter
import math 
from point import point

MAX_WIDTHSIZE = 500     #210 mm
MAX_HEIGHTSIZE = 500    #297 mm
SCALE = 70
PRECISION = 10

#increasing scale
def plus(event):
    #some code, which cleaning Canvas
    k += 10
    create_graphic(panel, graphic, function)

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

#creating graphic
def create_graphic(panel, graphic, function):
    for i in range(-250 * PRECISION, 250 * PRECISION + 1):
        j = i / PRECISION
        try:
            p = point(j * SCALE, -func(j, function) * SCALE)
            graphic.append(p)
        except ZeroDivisionError:
            continue
            
    draw_graphic(graphic, panel)
    return panel
        
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
panel = create_graphic(panel, graphic, function)

root.bind('<i>', plus)   #increase
root.bind('<d>', minus)  #degrease
root.mainloop()