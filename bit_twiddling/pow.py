def pow(x, y):
    "Given a double x and an integer y, compute x**y"
    s = 1
    while y:
        if y & 1:
            s *= x
        x *= x
        y >>= 1
    return s

assert pow(2, 4) == 2**4
assert pow(1, 0) == 1**0
assert pow(4, 8) == 4**8
assert pow(1, 10) == 1**10
assert pow(10, 1) == 10**1

