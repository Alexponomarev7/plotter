#! /usr/bin/env python3

from subprocess import *
import sys
from os import path

sys.path.append(path.sep.join(path.abspath(__file__).split(path.sep)[:-3] + ['src']))

import grapher
import bezier as bz

def graph(name, function, x_pos, y_pos, scale):
    grapher.main(name, function[0], x_pos, y_pos, scale)


def bezier(name, p_list):
    bz.main(name, p_list)
