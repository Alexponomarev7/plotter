#! /usr/bin/env python3

from subprocess import *

def graph(name, f_list):
    call(["cp", "img/graph.gif", "img/" + name + ".gif"])
  

def bezier(name, p_list):
    call(["cp", "img/bezier.gif", "img/" + name + ".gif"])
