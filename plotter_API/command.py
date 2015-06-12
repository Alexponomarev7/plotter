# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.
# Class command for creating code for API


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
        self.args = list(map(str, self.args))

        return types[self.id] + '(' + ", ".join(self.args) + ')'
