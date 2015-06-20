#! /usr/bin/env python3

from time import *

with open('test.txt', 'w') as f:
    print('Test', file=f)
    
sleep(5)
