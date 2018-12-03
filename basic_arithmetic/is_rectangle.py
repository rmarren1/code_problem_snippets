import math

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def is_rectangle(a, b, c, d):
    x_med = (a.x + b.x + c.x + d.x) / 4
    y_med = (a.y + b.y + c.y + d.y) / 4
    med = point(x_med, y_med)
    dists = map(lambda x: dist(x, med), [a, b, c, d])
    d = next(dists)
    for i in dists:
        if not math.isclose(i, d):
            return False
    return True

assert     is_rectangle(point(0, 0), point(0, 1), point(1, 0), point(1, 1))
assert not is_rectangle(point(0, 0), point(0, 2), point(1, 0), point(1, 1))
assert     is_rectangle(point(-1, -3), point(-1, 10), point(15, -3), point(15, 10))
assert not is_rectangle(point(0, 0), point(0, 2), point(1, 0), point(1, 1))
