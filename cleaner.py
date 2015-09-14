#!/usr/bin/env python3
import os, sys, glob, time

dir_name =  os.path.sep.join(os.path.abspath(sys.argv[0]).split(os.path.sep)[:-1])
#print(dir_name)

cur_time = time.time()
expire_time = 5 * 60 # 5 minutes

for d in ["tasks", "cnc", "img"]:
    for f in glob.glob(dir_name + os.path.sep + d + os.path.sep + "*"):
        if cur_time - os.path.getmtime(f) > expire_time:
            os.remove(f)
