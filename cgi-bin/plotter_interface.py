#! /usr/bin/env python3

from subprocess import *
import sys
from os import path

from lib.graph import grapher, bezier as bz
from lib import const

def graph(name, function, x_pos, y_pos, scale):
    grapher.main(name, function[0], x_pos, y_pos, scale / 10 * const.PIXELS_PER_MM)


def bezier(name, p_list):
    bz.main(name, p_list)
