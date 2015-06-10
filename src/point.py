class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def sumspoint(a, b, t):
    return point(b.x * t + a.x * (1 - t), b.y * t + a.y * (1 - t))