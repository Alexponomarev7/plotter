# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.
# Class command for creating code for API


types = [   'api.begin', 
            'api.end', 
            'api.draw_line',
            'api.draw_polygon', 
            'api.draw_ellipse', 
            'api.draw_polyline', 
            'api.draw_rect', 
            'api.draw_text']


class command:
    def __init__(self, id, args):
        self.id = id
        self.args = args

    def __str__(self):
        self.args = list(map(str, self.args))

        return types[self.id] + '(' + ", ".join(self.args) + ')'
