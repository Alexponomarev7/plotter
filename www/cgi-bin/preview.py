#! /usr/bin/env python3
import cgi
import html
import os
import http.cookies
import time

import plotter_interface as pl

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
seed = cookie.get("seed")

form = cgi.FieldStorage()
img_type = form.getvalue("img_type")

formulas = []

for Key in form.keys():
    key = str(Key)
    if key.startswith("formula"):
        index = int(key[7:])
        formulas.append((index, str(form.getvalue(key))))

formulas.sort()
formulas = list(map(lambda t: t[1], formulas))

if seed is not None:
    if img_type == "graph":
        pl.graph(seed.value, formulas)
    else:
        pl.bezier(seed.value, list(map(lambda s: tuple(map(float, s.split(","))), formulas)))

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
                <p>Number of formulas: """ + str(len(formulas)) + """
                <img src="/img/""" + seed.value + """.gif" />
                <form action="/cgi-bin/print.py">
                    <button>Print</button>
                </form>
            </body>
        </html>
    """)
