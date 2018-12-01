def plus(x, y):
    "Add together two non-negative integers only using bitwise operations."
    if y == 0:
        return x
    z = x ^ y
    carry = x & y
    return plus(z, carry << 1)

assert plus(0, 1) == 1
assert plus(1, 0) == 1
assert plus(0, 0) == 0
assert plus(12345, 678910) == 12345 + 678910
assert plus(2, 3) == 5
assert plus(10, 10) == 20
