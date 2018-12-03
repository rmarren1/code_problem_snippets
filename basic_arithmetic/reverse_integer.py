def reverse(x):
    sign = x >= 0
    x = abs(x)
    rev = int("".join(list(reversed(str(x)))))
    return rev if sign else -rev

assert reverse(123) == 321
assert reverse(-123) == -321
assert reverse(1) == 1
assert reverse(-1) == -1
assert reverse(0) == 0
