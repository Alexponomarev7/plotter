#! /usr/bin/env python3

import os
import sys

def log(string):
    return print(os.getpid(), string, file=sys.stderr)


