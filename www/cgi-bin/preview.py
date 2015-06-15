#! /usr/bin/env python3
import cgi
import html
import os
import sys
import http.cookies
import time

import plotter_interface as pl

from os import path

# print(__file__, file=sys.stderr)

sys.path.append(path.sep.join(path.abspath(__file__).split(path.sep)[:-3] + ['src']))
from point import *

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
seed = cookie.get("seed")

form = cgi.FieldStorage()

task_type = form.getvalue("task_type")
# min_x = float(form.getvalue("min_x"))
# min_y = float(form.getvalue("min_y"))
# max_x = float(form.getvalue("max_x"))
# max_y = float(form.getvalue("max_y"))

objects = [None] * int(form.getvalue("num_of_objects"))

if task_type == "graph":
    for i in range(len(objects)):
        objects[i] = str(form.getvalue('formula_' + str(i), '0'))
elif task_type == "bezier":
    for i in range(len(objects)):
        objects[i] = point(float(form.getvalue('x_' + str(i), '0')), float(form.getvalue('y_' + str(i), '0')))

print(objects, file=sys.stderr)

if seed is not None:
    if task_type == "graph":
        x_pos = float(form.getvalue("x_pos", 0))
        y_pos = float(form.getvalue("y_pos", 0))
        scale = float(form.getvalue("scale", 1))
        pl.graph(seed.value, objects, x_pos, y_pos, scale)
    elif task_type == "bezier":
        pl.bezier(seed.value, objects)

if seed is None:
    print("Set-cookie: seed=", time.time(), sep='')

print("Content-type: text/html\n")

if seed is None:
    print("""<!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>Plotter error</title>
            </head>
            <body>
                <p>
                    An error occured. Please reload page.
                </p>
            </body>
        </html>
    """)
else:
    print("""<!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>Plotter preview</title>
            </head>
            <body>
                <h1>Preview</h1>
                <p>Number of formulas: """ + str(len(objects)) + """</p>
                <img width="800" src="/img/""" + seed.value + """.gif" />
                <button onclick="window.location.href='/cgi-bin/print.py'">
                    Print
                </button>
                <button onClick="history.go(-1); return false;">
                    Go back
                </button>
            </body>
        </html>
    """)
