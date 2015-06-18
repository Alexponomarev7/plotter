#!/bin/bash
if [ -f .lock ] ; then
    rm .lock
fi

rm img/*.*.gif
rm tasks/*.*.py

# python3 -m http.server --cgi 1998
./server.py
