#! /usr/bin/env python3

from numpy import *
from ..graph.point import point
from . import glyphs as gl
from .driver import Driver

class API:
    
    def __init__(self, filename):
        self.drv = Driver(filename)
        self.matrices = []
        self.reset_matrix()

    def R(self, phi):
        return matrix([[cos(phi), -sin(phi), 0],
                [sin(phi), cos(phi), 0], 
                [0, 0, 1]])

    def T(self, x, y):
        return matrix([[1, 0, x], [0, 1, y], [0, 0, 1]])

    def S(self, sx, sy):
        return matrix([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

    def transform(self, pt, matr=None):
    #    print('Before:', pt)
        if matr is None:
            matr = self.get_current_matrix()
        P = matr * matrix([pt.x, pt.y, 1]).transpose()
        ans = point(P.tolist()[0][0], P.tolist()[1][0])
    #    print('After: ', ans)
    #    print(matr)
        return ans

    def split_into_polylines(self, seq):
        g = []
        for el in seq:
            if el is None:
                yield g
                g = []
            else:
                g.append(point(el[0], el[1]) if type(el) is not point else el)
        yield g


    def default_matrix(self):
        return matrix(eye(3))

    def reset_matrix(self):
        self.matrices[:] = [self.default_matrix()]

    def add_transform(self, t):
    #    print(t)
        self.matrices[-1] = t * self.matrices[-1]
    #    print(get_current_matrix())

    def push_matrix(self, matr):
        self.matrices.append(matr)
    #    print(get_current_matrix())

    def dup_matrix(self):
        self.push_matrix(self.get_current_matrix())

    def pop_matrix(self):
        if len(self.matrices) > 1:
            self.matrices.pop()
        else:
            self.reset_matrix()

    def get_current_matrix(self):
        return self.matrices[-1]

    # def begin(fname):
    #     drv.start_document(fname)
    #     reset_matrix()

    # def end():
    #     drv.end_document()
    def close(self):
        self.drv.close()

    def draw_line(self, start, end):
        if type(start) is tuple:
            start = point(start[0], start[1])
        if type(end) is tuple:
            end = point(end[0], end[1])
        t_start = self.transform(start)
        t_end = self.transform(end)
        self.drv.move_to(t_start.x, t_start.y)
        self.drv.line_to(t_end.x, t_end.y)

    def draw_polygon(self, point_list):
        if len(point_list) < 2:
            return
        t_point_list = list(map(self.transform, point_list))
        self.drv.draw_polygon(t_point_list)

    def draw_ellipse(self, x1, y1, x2, y2):
        p1 = point(x1, y1)
        p2 = point(x2, y2)
        center = point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

        rx = (x2 - x1) / 2
        ry = (y2 - y1) / 2

        point_list = [self.transform(point(cos(i / 180 * pi), sin(i / 180 * pi)), 
            self.T(center.x, center.y) * self.S(rx, ry)) for i in range(360)]
        self.draw_polygon(point_list)

    def draw_polyline(self, point_list):
        if len(point_list) < 2:
            return
        t_point_list = list(map(self.transform, point_list))
        self.drv.draw_polyline(t_point_list)

    def draw_rectangle(self, x1, y1, x2, y2):
        self.draw_polygon([point(x1, y1), point(x1, y2), point(x2, y2), point(x2, y1)])

    def draw_text(self, text, x, y, glyph_width=None, glyph_height=None):
        if glyph_width is None:
            glyph_width = 11
            glyph_height = 14
        elif glyph_height is None:
            glyph_height = glyph_width
            glyph_width = (11. / 14.) * glyph_height

        m = self.T(x, y) * self.S(glyph_width / gl.GLYPH_WIDTH, glyph_height / gl.GLYPH_HEIGHT)
        
        for symbol in text:
            if symbol not in gl.glyphs:
                symbol = ' '
            polylines = self.split_into_polylines(gl.glyphs[symbol])
            for pl in polylines:
                self.draw_polyline(list(map(lambda x: self.transform(x, m), pl)))
            m = self.T(glyph_width, 0) * m

    # Added for compability with ImageDraw from PILLOW
    def line(self, points, color=None):
        self.draw_line((points[0], points[1]), (points[2], points[3]))

    def text(self, pt, text, color=None, font=None):
        self.draw_text(text, pt[0], pt[1])

    def rectangle(self, points, outline=None, filling=None):
        self.draw_rectange(points[0], points[1], points[2], points[3])

    def draw_polylines(self, pt_iter):
        for polyline in self.split_into_polylines(pt_iter):
            self.draw_polyline(polyline)
