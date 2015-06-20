#! /usr/bin/env python3

import os

X_REAL_RESOLUTION = 297
Y_REAL_RESOLUTION = 210

PIXELS_PER_MM = 4

IMAGE_PATH = "img/"
TASKS_PATH = "tasks/"
CNC_PATH = "cnc/"

IMAGE_EXT = ".png"
TASKS_EXT = ".py"
CNC_EXT = ".cnc"

SITE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# for lib.graph.grapher
PRECISION_MULTIPLIER = 4
