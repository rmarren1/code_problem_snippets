from plus import plus
def mul(x, y):
    "Multiply two non-negative integers using only bitwise operations"
    z = 0
    while y:
        if y & 1:
            z = plus(z, x)
        y >>= 1
        x <<= 1
    return z

assert mul(0, 1) == 0
assert mul(0, 0) == 0
assert mul(1, 0) == 0
assert mul(2, 3) == 6
assert mul(10, 10) == 100
assert mul(1000, 1) == 1000
