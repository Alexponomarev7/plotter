#! /usr/bin/env python3

from ..graph.point import point
from lib import const

fout = None
UP = False
DOWN = True
pencil_state = DOWN

def transform_x(x):
    return x / const.PIXELS_PER_MM

def transform_y(y):
    return y / const.PIXELS_PER_MM

def start_document(fname):
    global fout
    fout = open(fname, 'w')
    print('%', file=fout)
    print('G21', file=fout)
    pencil_up()

def pencil_up():
    global pencil_state
    if pencil_state is DOWN:
        print('G00', 'Z20.0', file=fout)
        pencil_state = UP

def pencil_down():
    global pencil_state
    if pencil_state is UP:
        print('G00', 'Z33.0', file=fout)
        pencil_state = DOWN

def line_to(x, y, in_polygon=False):
    if not in_polygon:
        pencil_down()
    print('G01', 'X%.8f' % transform_x(x), 'Y%.8f' % transform_y(y), file=fout)
    if not in_polygon:
        pencil_up()

def move_to(x, y):
    pencil_up()
    print('G00', 'X%.8f' % transform_x(x), 'Y%.8f' % transform_y(y), file=fout)

def draw_polygon(point_list):
    pencil_up()
    move_to(point_list[-1].x, point_list[-1].y)
    pencil_down()
    for point in point_list:
        line_to(point.x, point.y, True)
    pencil_up()

def draw_polyline(point_list):
    pencil_up()
    move_to(point_list[0].x, point_list[0].y)
    pencil_down()
    for point in point_list[1:]:
        line_to(point.x, point.y, True)
    pencil_up()

def end_document():
    print('%', file=fout)
    fout.close()