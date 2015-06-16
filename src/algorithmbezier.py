# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

from point import point

# Vector's radius
def sumspoint(a, b, t):
    return point(b.x * t + a.x * (1 - t),
                 b.y * t + a.y * (1 - t))


def bezier(P, t):
    if len(P) == 1:
        return P[0]
    else:
        newP = []
        for i in range(len(P) - 1):
            newP.append(sumspoint(P[i], P[i + 1], t))
        return bezier(newP, t)
    
  
def algorithmbezier(P):
    points = []
    for i in range(100):
        t = i / 100
        points.append(bezier(P, t))

    return points