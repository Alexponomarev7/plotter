# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.
#class command for creating code for API

types = ['pencilUp',
         'pencilDown',
         'moveTo',
         'drawOval',
         'drawRectangle',
         'drawPolygon',
         'print'
         'pause']
         
class command:
    def __init__(self, id, args):
        self.id = id
        self.args = args
    def __str__(self):
        for i in range(len(self.args)):
            self.args[i] = str(self.args[i])
            
        return types[self.id] + '(' + ", ".join(self.args) + ')'
    
