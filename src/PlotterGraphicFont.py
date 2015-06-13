__author__ = 'HagRead-Only'

from tkinter import *

root = Tk()
root.title("PlotterGraphicFont")
cnv = Canvas(root, width=260, height=280)
cnv.pack()

cnv.create_text(75, 15, text="Enter real number or axis.")
cnv.create_text(70, 35, text="Type 'exit' to close app.")

line = Text(root, height=1, width=11, font="Calibri")
line.place(x=10, y=55)

x = 10
y = 75


def draw_0(x, y):
    cnv.create_line(x, y, x + 8, y)
    cnv.create_line(x + 8, y, x + 8, y + 14)
    cnv.create_line(x + 8, y + 14, x, y + 14)
    cnv.create_line(x, y + 14, x, y)


def draw_1(x, y):
    cnv.create_line(x + 1, y, x + 4, y)
    cnv.create_line(x + 4, y, x + 4, y + 14)
    cnv.create_line(x, y + 14, x + 8, y + 14)


def draw_2(x, y):
    cnv.create_line(x, y, x + 8, y)
    cnv.create_line(x + 8, y, x + 8, y + 7)
    cnv.create_line(x + 8, y + 7, x, y + 7)
    cnv.create_line(x, y + 7, x, y + 14)
    cnv.create_line(x, y + 14, x + 8, y + 14)


def draw_3(x, y):
    cnv.create_line(x, y, x + 8, y)
    cnv.create_line(x + 8, y, x + 8, y + 14)
    cnv.create_line(x + 8, y + 14, x, y + 14)
    cnv.create_line(x, y + 7, x + 8, y + 7)


def draw_4(x, y):
    cnv.create_line(x, y, x, y + 7)
    cnv.create_line(x, y + 7, x + 8, y + 7)
    cnv.create_line(x + 8, y, x + 8, y + 14)


def draw_5(x, y):
    cnv.create_line(x + 8, y, x, y)
    cnv.create_line(x, y, x, y + 7)
    cnv.create_line(x, y + 7, x + 8, y + 7)
    cnv.create_line(x + 8, y + 7, x + 8, y + 14)
    cnv.create_line(x + 8, y + 14, x, y + 14)


def draw_6(x, y):
    cnv.create_line(x + 8, y, x, y)
    cnv.create_line(x, y, x, y + 14)
    cnv.create_line(x, y + 14, x + 8, y + 14)
    cnv.create_line(x + 8, y + 14, x + 8, y + 7)
    cnv.create_line(x + 8, y + 7, x, y + 7)


def draw_7(x, y):
    cnv.create_line(x, y, x + 8, y)
    cnv.create_line(x + 8, y, x + 4, y + 7)
    cnv.create_line(x + 4, y + 7, x + 4, y + 14)


def draw_8(x, y):
    cnv.create_line(x, y, x + 8, y)
    cnv.create_line(x + 8, y, x + 8, y + 14)
    cnv.create_line(x + 8, y + 14, x, y + 14)
    cnv.create_line(x, y + 14, x, y)
    cnv.create_line(x, y + 7, x + 8, y + 7)


def draw_9(x, y):
    cnv.create_line(x, y + 14, x + 8, y + 14)
    cnv.create_line(x + 8, y + 14, x + 8, y)
    cnv.create_line(x + 8, y, x, y)
    cnv.create_line(x, y, x, y + 7)
    cnv.create_line(x, y + 7, x + 8, y + 7)


def draw_x(x, y):
    cnv.create_line(x, y, x + 8, y + 14)
    cnv.create_line(x + 8, y, x, y + 14)


def draw_y(x, y):
    cnv.create_line(x, y, x, y + 7)
    cnv.create_line(x, y + 7, x + 8, y + 7)
    cnv.create_line(x + 8, y, x + 8, y + 14)
    cnv.create_line(x + 8, y + 14, x, y + 14)


def draw_point(x, y):
    cnv.create_line(x + 4, y + 13, x + 5, y + 13)
    cnv.create_line(x + 5, y + 13, x + 5, y + 14)
    cnv.create_line(x + 5, y + 14, x + 4, y + 14)


def draw_minus(x, y):
    cnv.create_line(x, y + 7, x + 8, y + 7)


def click():
    global x, y
    x = 10
    y += 20

    s = line.get(0.1, END).strip()

    if s == "exit":
        raise SystemExit(0)

    for i in range(len(s)):
        if s[i] == '.':
            draw_point(x, y)
        elif s[i] == '-':
            draw_minus(x, y)
        else:
            exec("draw_" + s[i] + "(" + str(x) + ", " + str(y) + ")")
        x += 11

    line.delete(0.1, END)


btn = Button(root, text="ok", width=4, height=1, font="Calibri", command=click)
btn.place(x=110, y=50)

root.mainloop()

# 0 1 2 3 4 5 6 7 8 9 x y . -
