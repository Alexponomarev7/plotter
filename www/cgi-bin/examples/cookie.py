#!/usr/bin/env python3
import os
import time
import http.cookies

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
sid = cookie.get("sid")
if sid is None:
    sid = str(time.time())
    print("Set-cookie: sid=" + sid)
    print("Content-type: text/html\n")
    print("Cookies!!!")
else:
    print("Content-type: text/html\n")
    print("Cookies:")
    print(sid.value)
