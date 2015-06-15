#! /usr/bin/env python3

from subprocess import *
import sys
from os import path

sys.path.append(path.sep.join(path.abspath(__file__).split(path.sep)[:-3] + ['src']))

import grapher
import bezier

def graph(name, function):
    grapher.main(name, function)


def bezier(name, p_list):
    bezier.main(name, p_list)