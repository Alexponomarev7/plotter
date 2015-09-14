#!/bin/bash
if [ -f .lock ] ; then
    rm .lock
fi

./cleaner.py

# python3 -m http.server --cgi 1998
./server.py
