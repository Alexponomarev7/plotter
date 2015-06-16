#! /usr/bin/env python3

import api
import math

api.begin('test3.cnc')
api.dup_matrix()
api.add_transform(api.R(math.pi / 3))
api.draw_ellipse(-100, -200, 100, 200)
api.pop_matrix()
api.draw_ellipse(-100, -100, 100, 100)
api.end()
