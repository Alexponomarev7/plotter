#! /usr/bin/env python3
import cgi
import html
import os
import sys
import http.cookies
import time
import traceback

import plotter_interface as pl

from os import path

# print(__file__, file=sys.stderr)

sys.path.append(path.sep.join(path.abspath(__file__).split(path.sep)[:-3] + ['src']))
from point import *

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
seed = cookie.get("seed")

time_start = time.time()

form = cgi.FieldStorage()

task_type = form.getvalue("task_type")
# min_x = float(form.getvalue("min_x"))
# min_y = float(form.getvalue("min_y"))
# max_x = float(form.getvalue("max_x"))
# max_y = float(form.getvalue("max_y"))

objects = [None] * int(form.getvalue("num_of_objects"))

errors = False
try:
    if task_type == "graph":
        for i in range(len(objects)):
            objects[i] = str(form.getvalue('function_' + str(i), '0'))
            x_pos = float(form.getvalue("x_pos", 0))
            y_pos = float(form.getvalue("y_pos", 0))
            scale = int(form.getvalue("scale", 100))
            # print(x_pos, y_pos, scale, file=sys.stderr)
            pl.graph(seed.value, objects, x_pos, y_pos, scale)
    elif task_type == "bezier":
        for i in range(len(objects)):
            objects[i] = point(float(form.getvalue('x_' + str(i), '0')), float(form.getvalue('y_' + str(i), '0')))

    print(objects, file=sys.stderr)

    if seed is not None:
        if task_type == "graph":
            x_pos = float(form.getvalue("x_pos", 0))
            y_pos = float(form.getvalue("y_pos", 0))
            scale = float(form.getvalue("scale", 1))
            print(x_pos, y_pos, scale, file=sys.stderr)
            pl.graph(seed.value, objects, x_pos, y_pos, scale)
        elif task_type == "bezier":
            pl.bezier(seed.value, objects)

except Exception as e:
    print(type(e), file=sys.stderr)
    print(e, file=sys.stderr)
    print(traceback.format_exc(), file=sys.stderr)
    errors = True

time_end = time.time()

if seed is None:
    print("Set-cookie: seed=", time.time(), sep='')

print("Content-type: text/html\n")

if seed is None:
    print("ERROR: seed is None", file=sys.stderr)
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
                <button onClick="location.reload(); return false;">
                    Reload
                </button>
            </body>
        </html>
    """)
elif errors:
    print("""<!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>Plotter error</title>
		<style>
 		  body {
   		    background: black; /* Цвет фона */
    		    color: white; /* Цвет текста */
  		  }
  		</style>
            </head>
            <body>
                <p>
                    An error occured while processing the task. Please go back and check out your input.
                </p>
                <button onClick="history.go(-1); return false;">
                    Go back
                </button>
		<br />
		<br />
		<img src="/img/cat.jpg" alt="ГОВНОКОД!!!"/>
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
                <img border="1px" width="800" src="/img/""" + seed.value + """.gif" />
                <br />
                <button onclick="window.location.href='/cgi-bin/print.py'">
                    Print
                </button>
                <button onClick="history.go(-1); return false;">
                    Go back
                </button>
                <a href="/img/""" + seed.value + """.gif" download>Save image</a>
                <p>Time: """ + str(time_end - time_start) + """</p>
            </body>
        </html>
    """)
