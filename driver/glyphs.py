#! /usr/bin/env python3


from point import *

def split_into_polylines(seq):
    g = []
    for el in seq:
        if el is None:
            yield g
            g = []
        else:
            g.append(point(el[0], el[1]))
    yield g

GLYPH_WIDTH = 11
GLYPH_HEIGHT = 14

glyphs = dict()
glyphs['0'] = [(0, 0), (8, 0), (8, 14), (0, 14), (0, 0)]
glyphs['1'] = [(1, 0), (4, 0), (4, 14), None, (0, 14), (8, 14)]
glyphs['2'] = [(0, 0), (8, 0), (8, 7), (0, 7), (0, 14), (8, 14)]
glyphs['3'] = [(0, 0), (8, 0), (8, 14), (0, 14), None, (0, 7), (8, 7)]
glyphs['4'] = [(0, 0), (0, 7), (8, 7), None, (8, 0), (8, 14)]
glyphs['5'] = [(8, 0), (0, 0), (0, 7), (8, 7), (8, 14), (0, 14)]
glyphs['6'] = [(8, 0), (0, 0), (0, 14), (8, 14), (8, 7), (0, 7)]
glyphs['7'] = [(0, 0), (8, 0), (4, 7), (4, 14)]
glyphs['8'] = [(0, 0), (8, 0), (8, 14), (0, 14), (0, 0), None, (0, 7), (8, 7)]
glyphs['9'] = [(0, 14), (8, 14), (8, 0), (0, 0), (0, 7), (8, 7)]

glyphs['X'] = glyphs['x'] = [(0, 0), (8, 14), None, (8, 0), (0, 14)]
glyphs['Y'] = glyphs['y'] = [(0, 0), (0, 7), (8, 7), None, (8, 0), (8, 14), (0, 14)]

glyphs['.'] = [(4, 13), (5, 13), (5, 14), (4, 14), (4, 13)]
glyphs['-'] = [(0, 7), (8, 7)]

glyphs[' '] = []
# result = list(split_into_polylines(glyphs[x]))