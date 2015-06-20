# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.


class point:
    # Class's constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
        
    def __repr__(self):
        return str(self)
