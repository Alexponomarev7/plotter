# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

# import tkinter
from math import sqrt, sin, cos, pi
from math import tan as tg, atan as arctg, asin as arcsin, acos as arccos
from .point import point
from .drawing import draw
from .. import const, web, safe_checker
from ..log import *
import sys, traceback
import itertools

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

def arcctg(x):
    return pi - arctg(x)

def sgn(x):
    return 0 if x == 0 else 1 if x > 0 else -1

def recursive_function_stub(x):
    raise ArithmeticError

# Creating graphic
def create_graphic(function, function_number, x_pos, y_pos, SCALE, name, preview, percent_edges=None):
#    graphic = []
    func_backup, f[function_number] = f[function_number], recursive_function_stub

    min_x = -(WIDTH / (2 * SCALE))
    max_x = WIDTH / (2 * SCALE)
    x = min_x
    dx = 1 / PRECISION
    last = 0    

    old_percent_done = -1

    while x <= max_x:
        x += dx        
        try:
            percent_done = int((x - min_x) * 100 / (max_x - min_x))
            if percent_done != old_percent_done and preview:
                web.update_status("Completed " + 
                        str(int(percent_done / 100.0 * (percent_edges[1] - percent_edges[0]) + 
                            percent_edges[0])) + "%")
                old_percent_done = percent_done
            
            new_y = -func(x, function)
            if type(new_y) is complex:
                raise ArithmeticError
            p = point(x * SCALE + WIDTH / 2,
                new_y * SCALE + HEIGHT / 2)
            if abs(last - new_y) / dx >= CHECK:
                yield None
            last = new_y
            yield p
        except NameError:
            raise
        except SyntaxError:
            raise
        except:
            yield None
    
    f[function_number] = func_backup
    yield None

#    return graphic
#    draw(graphic, name, "graphic", SCALE)

# Creating GUI
def main(name, function_list, x_pos, y_pos, SCALE, preview):
    global PRECISION
    PRECISION = int(SCALE) * const.PRECISION_MULTIPLIER
    
    graphic_iter = []

    f[:] = [func_decorator(function[0]) for function in function_list]

    functions = 0
    for function in function_list:
        safe_checker.check(function[0])
        if function[1]:
            functions += 1

    cur_function = 0
    cur_rendering_function = 0
    for function in function_list:
        if function[1]:
            point_iter = create_graphic(function[0], cur_function, x_pos, y_pos, SCALE, name, 
                    preview, (cur_rendering_function  * 100 / functions, (cur_rendering_function + 1) * 100 / functions))    
            cur_rendering_function += 1
            graphic_iter += [point_iter]
        cur_function += 1
    log("grapher.main") 
    log(preview)
    draw(itertools.chain.from_iterable(graphic_iter), name, "graphic", SCALE, {}, preview)
