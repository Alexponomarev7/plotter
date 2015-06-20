#! /usr/bin/env python3

from ..graph.point import point
from lib import const

class Driver:

    UP = False
    DOWN = True
    
    def __init__(self, filename):
        self.fout = None
        self.pencil_state = Driver.DOWN
        self.__start_document(filename)

    def transform_x(self, x):
        return x / const.PIXELS_PER_MM

    def transform_y(self, y):
        return y / const.PIXELS_PER_MM

    def __start_document(self, fname):
        self.fout = open(fname, 'w')
        print('%', file=self.fout)
        print('G21', file=self.fout)
        self.pencil_up()

    def pencil_up(self):
        if self.pencil_state is Driver.DOWN:
            print('G00', 'Z20.0', file=self.fout)
            self.pencil_state = Driver.UP

    def pencil_down(self):
        if self.pencil_state is Driver.UP:
            print('G00', 'Z33.0', file=self.fout)
            self.pencil_state = Driver.DOWN

    def line_to(self, x, y, in_polygon=False):
        if not in_polygon:
            self.pencil_down()
        print('G01', 'X%.8f' % self.transform_x(x), 'Y%.8f' % self.transform_y(y), file=self.fout)
        if not in_polygon:
            self.pencil_up()

    def move_to(self, x, y):
        self.pencil_up()
        print('G00', 'X%.8f' % self.transform_x(x), 'Y%.8f' % self.transform_y(y), file=self.fout)

    def draw_polygon(self, point_list):
        self.pencil_up()
        self.move_to(point_list[-1].x, point_list[-1].y)
        self.pencil_down()
        for point in point_list:
            self.line_to(point.x, point.y, True)
        self.pencil_up()

    def draw_polyline(self, point_list):
        self.pencil_up()
        self.move_to(point_list[0].x, point_list[0].y)
        self.pencil_down()
        for point in point_list[1:]:
            self.line_to(point.x, point.y, True)
        self.pencil_up()

    def __end_document(self):
        print('%', file=self.fout)
        self.fout.close()

    def close(self):
        self.__end_document()
