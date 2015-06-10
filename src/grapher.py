from tkinter import *
from math import *
from point import point

MAX_WIDTHSIZE = 500
MAX_HEIGHTSIZE = 500

def plus(event):
    global panel, graphic, function, k
    panel.delete("all")
    k += 10
    create_graphic(panel, graphic, function, k)

def func(x, function):
    function.replace('x', str(x))
    return eval(function)

def draw_graphic(p, panel):
    for i in range(len(p) - 1):
        panel.create_line(p[i].x + 250, p[i].y + 250, p[i + 1].x + 250, p[i + 1].y + 250, fill="red", tag="group")
     
def create_graphic(panel, graphic, function, k):
    for i in range(-250 * 10, 250 * 10 + 1):
        j = i / 10
        try:
            p = point(j * k, -func(j, function) * k)
            graphic.append(p)
        except ZeroDivisionError:
            continue
            
    draw_graphic(graphic, panel)
    return panel
        
    
root = Tk()
panel = Canvas(root, width=MAX_WIDTHSIZE, height=MAX_HEIGHTSIZE)
panel.grid(row = 0, column = 0)

graphic = []
k =  70
function = input('y = ')
panel.create_line(MAX_HEIGHTSIZE / 2, 0, MAX_HEIGHTSIZE / 2, MAX_WIDTHSIZE, fill="gray50")
panel.create_line(0, MAX_HEIGHTSIZE / 2, MAX_WIDTHSIZE, MAX_HEIGHTSIZE / 2, fill="gray50")

panel = create_graphic(panel, graphic, function, k)

root.bind('<q>', plus)
root.mainloop()