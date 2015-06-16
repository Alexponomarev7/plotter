#! /usr/bin/env python3

import math
import api

api.begin('/home/xenon/shared/test4.cnc')
api.dup_matrix()
api.add_transform(api.R(math.pi / 3))
api.draw_text('xy1234567890-.', 10, 10, 10, 18)
api.pop_matrix()
api.end()
