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
min_x = float(form.getvalue("min_x"))
min_y = float(form.getvalue("min_y"))
max_x = float(form.getvalue("max_x"))
max_y = float(form.getvalue("max_y"))

objects = []

if task_type == "graph":
    for Key in form.keys():
        key = str(Key)
        if key.startswith("function_"):
            objects.append((int(key.split('_')[1]), str(form.getvalue(key))))
    objects = list(map(lambda pair: pair[1], sorted(objects)))
elif task_type == "bezier":
    xs = []
    ys = []
    for Key in form.keys():
        key = str(Key)
        if key.startswith("x_"):
            xs.append((int(key.split('_')[1]), float(form.getvalue(key))))
        if key.startswith("y_"):
            ys.append((int(key.split('_')[1]), float(form.getvalue(key))))
    xs.sort()
    ys.sort()
    objects = [(xs[i], ys[i]) for i in range(min(len(xs), len(ys)))]
    
if seed is not None:
    if task_type == "graph":
        pl.graph(seed.value, objects) #, min_x, max_x, min_y, max_y)
    elif task_type == "bezier":
        pl.bezier(seed.value, objects) #, min_x, max_x, min_y, max_y)

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
                <img src="/img/""" + seed.value + """.gif" />
                <form action="/cgi-bin/print.py">
                    <button>Print</button>
                </form>
            </body>
        </html>
    """)
