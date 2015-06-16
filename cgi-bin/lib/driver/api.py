#! /usr/bin/env python3

from numpy import *
from ..graph.point import point
from . import driver as drv, glyphs as gl

def R(phi):
    return matrix([[cos(phi), -sin(phi), 0],
            [sin(phi), cos(phi), 0], 
            [0, 0, 1]])

def T(x, y):
    return matrix([[1, 0, x], [0, 1, y], [0, 0, 1]])

def S(sx, sy):
    return matrix([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

def transform(pt, matr=None):
#    print('Before:', pt)
    if matr is None:
        matr = get_current_matrix()
    P = matr * matrix([pt.x, pt.y, 1]).transpose()
    ans = point(P.tolist()[0][0], P.tolist()[1][0])
#    print('After: ', ans)
#    print(matr)
    return ans

def split_into_polylines(seq):
    g = []
    for el in seq:
        if el is None:
            yield g
            g = []
        else:
            g.append(point(el[0], el[1]))
    yield g


def default_matrix():
    return matrix(eye(3))

matrices = [default_matrix()]

def reset_matrix():
    matrices[:] = [default_matrix()]

def add_transform(t):
#    print(t)
    matrices[-1] = t * matrices[-1]
#    print(get_current_matrix())

def push_matrix(matr):
    matrices.append(matr)
#    print(get_current_matrix())

def dup_matrix():
    push_matrix(get_current_matrix())

def pop_matrix():
    if len(matrices) > 1:
        matrices.pop()
    else:
        reset_matrix()

def get_current_matrix():
    return matrices[-1]

def begin(fname):
    drv.start_document(fname)
    reset_matrix()

def end():
    drv.end_document()

def draw_line(start, end):
    t_start = transform(start)
    t_end = transform(end)
    drv.move_to(t_start.x, t_start.y)
    drv.line_to(t_end.x, t_end.y)

def draw_polygon(point_list):
    t_point_list = list(map(transform, point_list))
    drv.draw_polygon(t_point_list)

def draw_ellipse(x1, y1, x2, y2):
    p1 = point(x1, y1)
    p2 = point(x2, y2)
    center = point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

    rx = (x2 - x1) / 2
    ry = (y2 - y1) / 2

    point_list = [transform(point(cos(i / 180 * pi), sin(i / 180 * pi)), 
        T(center.x, center.y) * S(rx, ry)) for i in range(360)]
    draw_polygon(point_list)

def draw_polyline(point_list):
    t_point_list = list(map(transform, point_list))
    drv.draw_polyline(t_point_list)

def draw_rect(x1, y1, x2, y2):
    draw_polygon([point(x1, y1), point(x1, y2), point(x2, y2), point(x2, y1)])

def draw_text(text, x, y, glyph_width=None, glyph_height=None):
    if glyph_width is None:
        glyph_width = 11
        glyph_height = 14
    elif glyph_height is None:
        glyph_height = glyph_width
        glyph_width = (11. / 14.) * glyph_height

    m = T(x, y) * S(glyph_width / gl.GLYPH_WIDTH, glyph_height / gl.GLYPH_HEIGHT)
    
    for symbol in text:
        if symbol not in gl.glyphs:
            symbol = ' '
        polylines = split_into_polylines(gl.glyphs[symbol])
        for pl in polylines:
            draw_polyline(list(map(lambda x: transform(x, m), pl)))
        m = T(glyph_width, 0) * m

