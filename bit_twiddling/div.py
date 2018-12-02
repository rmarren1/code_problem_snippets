def div(x, y):
    "Find the quotient of x / y only using +, -, and bit operations."
    y_0 = y
    if x >= y:
        q = 1
        while x >= y << 1:
            y <<= 1
            q <<= 1
        return q + div(x-y, y_0)
    return 0

assert div(3, 2) == 3 // 2
assert div(0, 1) == 0 // 1
assert div(10, 2) == 10 // 2
assert div(1000, 2) == 1000 // 2
assert div(1000, 1) == 1000 // 1
