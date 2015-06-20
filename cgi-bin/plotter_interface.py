#! /usr/bin/env python3

from subprocess import *
import sys
from os import path

from lib.graph import grapher, bezier as bz
from lib.graph.point import *
from lib import const

def graph(name, functions, settings): # x_pos, y_pos, scale):
    x_pos, y_pos, scale = settings['x_pos'], settings['y_pos'], settings['scale']
    grapher.main(name, functions, x_pos, y_pos, scale / 10 * const.PIXELS_PER_MM, True)
    # print_task(name, task)

def bezier(name, p_list, settings):
    bz.main(name, list(map(lambda p: point(p.x * const.PIXELS_PER_MM, p.y * const.PIXELS_PER_MM), p_list)), settings, True)
    # print_task(name, task)

# def print_task(name, task):
#     fout = open(const.TASKS_PATH + name + ".py", 'w')
#     print("api.begin(\'cnc/" + name + ".cnc\')", file=fout)
# 
#     print("points =", task[1], '\n', file=fout)
#     
#     for elem in task[0]:
#         func_name = None
#         if elem[0] == "l":
#             func_name = "api.draw_line"
#         elif elem[0] == "t":
#             func_name = "api.draw_text"
#         elif elem[0] == "r":
#             func_name = "api.draw_rectangle"
#         print(func_name, elem[1], file=fout)
# 
#     print("for polyline in api.split_into_polylines(points):\n    api.draw_polyline(polyline)", file=fout)
# 
#     print("api.end()", file=fout)
#     fout.close()
