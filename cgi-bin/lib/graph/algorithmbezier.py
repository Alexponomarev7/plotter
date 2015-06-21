from .point import point
from .. import const, web

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
    
  
def algorithmbezier(P, preview):
    percent = -1
    for i in range(const.BEZIER_POINTS + 1):
        t = i / const.BEZIER_POINTS
        new_percent = int(t * 100)
        if preview and new_percent != percent:
            web.update_status("Completed %d%%" % new_percent)
            percent = new_percent
        yield bezier(P, t)

