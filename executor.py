#! /usr/bin/env python3

import sys
import os
import time

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
        exec(code, {'driver_dir': "/".join(os.path.abspath(__file__).split("/")[:-3] + ['driver'])})
        

def send_cnc():
    pass
    # Here must be code that sends .cnc file to plotter
    
def main():
    log("started")
    log("wait while unlocking...")
    while is_locked():
        time.sleep(1)
    lock()
    log("generating cnc")
    gen_cnc()
    log("sending cnc")
    send_cnc()
    log("done")
    unlock()
    log("stopped")
    
main()