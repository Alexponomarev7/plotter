#! /usr/bin/env python3
import http.cookies
import os
import sys
import subprocess

from os import path
from lib import const

os.chdir(const.SITE_DIR)

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
seed = cookie.get("seed").value

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
                    An error occured. Please go back and try again.
                </p>
            </body>
        </html>
    """)
    sys.exit(0)
    

print("""<!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8" />
            <title>Plotter</title>
        </head>
        <body>
            <h1>Printing now...</h1>""")

# subprocess.call("python3 cgi-bin/executor.py " + seed, shell=True)
pid = subprocess.Popen(["cgi-bin/executor.py", seed]).pid
print("<p>debug info: pid =", pid, "</p>")
print('<a href="index.py">Home</a>')
     
print("""<script>window.stop()</script>
        </body>
    </html>
""")

sys.exit(0)
