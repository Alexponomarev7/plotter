#! /usr/bin/env python3

import api

api.begin('test2.cnc')
api.draw_rect(100, 100, 200, 200)
api.draw_ellipse(100, 100, 200, 200)
api.end()
