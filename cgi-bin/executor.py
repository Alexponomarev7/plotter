#! /usr/bin/env python3

import sys
import os
import time

from lib.driver import api
from lib.graph import point

seed = sys.argv[1]

def log(string):
    return print(os.getpid(), string, file=sys.stderr)

def lock():
    open('.lock', 'a').close()
    log("locked")
    
def unlock():
    os.remove('.lock')
    log("unlocked")
    
def is_locked():
    return os.path.exists('.lock')

def gen_cnc():          
    filename = "tasks/" + seed + ".py"
    with open(filename, 'r') as f:
        code = compile(f.read(), filename, "exec")
        exec(code)
        

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
    except:
        print(sys.exc_info()[0])
    finally:
        unlock()
        log("stopped")
    
main()
