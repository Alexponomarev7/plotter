#! /usr/bin/env python3
import cgi
import html
import os
import sys
import http.cookies
import time
import traceback

import plotter_interface as pl
from lib.graph.point import point
from lib import const, web

os.chdir(const.SITE_DIR)

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
seed = cookie.get("seed")

# time_start = time.time()

form = cgi.FieldStorage()

task_type = form.getvalue("task_type")
# min_x = float(form.getvalue("min_x"))
# min_y = float(form.getvalue("min_y"))
# max_x = float(form.getvalue("max_x"))
# max_y = float(form.getvalue("max_y"))

objects = [None] * int(form.getvalue("num_of_objects"))
settings = dict()

if task_type == "graph":
    for i in range(len(objects)):
        objects[i] = (str(form.getvalue('function_' + str(i), '0')), bool(form.getvalue("draw_" + str(i), '')))
        settings["x_pos"] = float(form.getvalue("x_pos", 0))
        settings["y_pos"] = float(form.getvalue("y_pos", 0))
        settings["scale"] = int(form.getvalue("scale", 100))
elif task_type == "bezier":
    for i in range(len(objects)):
        objects[i] = point(float(form.getvalue('x_' + str(i), '0')), float(form.getvalue('y_' + str(i), '0')))
        settings["draw_anchor"] = bool(form.getvalue("draw_anchor", ''))

# print(objects, file=sys.stderr)

#     if seed is not None:
       
# time_end = time.time()

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

# elif error is not None:
#     print("""<!DOCTYPE html>
#         <html>
#             <head>
#                 <meta charset="utf-8" />
#                 <title>Plotter error</title>
#             </head>
#             <body>
#                 <p>
#                     An error occured while processing the task. Please go back and check out your input. <br /> """ + error[1] + os.getcwd() + """
#                 </p>
#                 <button onClick="history.go(-1); return false;">
#                     Go back
#                 </button>
#             </body>
#         </html>
#     """)
else:
    
    print("""<!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>Plotter preview</title>
                <script src="/js/jquery.min.js"></script>
            </head>
            <body>
                <h1>Preview</h1>
                <p>Number of formulas: """ + str(len(objects)) + """</p>
                <div id="status"></div>""" +
#                 <img border="1px" width="800" src="/img/""" + seed.value + """.gif" />
                """
                <br />
                <button onclick="window.location.href='/cgi-bin/print.py'">
                    Print
                </button>
                <button onClick="history.go(-1); return false;">
                    Go back
                </button>
                <a href="/""" + const.IMAGE_PATH + seed.value + const.IMAGE_EXT + """" download hidden>Save image</a>
    """) 
    sys.stdout.flush()

    try:
#        web.update_status("Test")
        if task_type == "graph":
            pl.graph(seed.value, objects, settings)
        elif task_type == "bezier":
            pl.bezier(seed.value, objects, settings)
        print("""<script>
                    $("#status").html(\'<img border="1px" width="800" src="/""" + 
                    const.IMAGE_PATH + seed.value + const.IMAGE_EXT + """" />\');
                    $("a").show();
                </script>""")

    except Exception as e:
        tb = traceback.format_exc()
        print(tb, file=sys.stderr)
        web.update_status(tb)

    print("""
            </body>
        </html>""")
    sys.stdout.flush()
