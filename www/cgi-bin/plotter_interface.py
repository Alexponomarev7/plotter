#! /usr/bin/env python3

from subprocess import *

def graph(name, f_list, min_x, max_x, min_y, max_y):
    call(["cp", "img/graph.gif", "img/" + name + ".gif"])
    call(["cp", "tasks/task.py", "tasks/" + name + ".py"])
  

def bezier(name, p_list, min_x, max_x, min_y, max_y):
    call(["cp", "img/bezier.gif", "img/" + name + ".gif"])
    call(["cp", "tasks/task.py", "tasks/" + name + ".py"])
