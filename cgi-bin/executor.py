#! /usr/bin/env python3

import sys
import os
import time
import traceback

from lib.driver import api
from lib.graph import point
from lib import const
from lib.log import *

import plotter_interface as pl

os.chdir(const.SITE_DIR)

seed = sys.argv[1]

def lock():
    open('.lock', 'a').close()
    log("locked")
    
def unlock():
    os.remove('.lock')
    log("unlocked")
    
def is_locked():
    return os.path.exists('.lock')

def gen_cnc():          
    filename = const.TASKS_PATH + seed + const.TASKS_EXT
    with open(filename, 'r') as f:
        #code = compile(f.read(), filename, "exec")
        #log("1")
        exec(f.read())
        #log("2")
        

def send_cnc():
    pass
    # Here must be code that sends .cnc file to plotter
    
def main():
    log("started")
    log(sys.path)
    log("wait while unlocking...")
    while is_locked():
        time.sleep(1)
    lock()
    try:
        log("generating cnc")
        gen_cnc()
        log("sending cnc")
        send_cnc()
        log("done")
    except Exception as e:
        log("ERROR")
        tb = traceback.format_exc()
        print(tb, file=sys.stderr)
    unlock()
    log("stopped")
    
main()
