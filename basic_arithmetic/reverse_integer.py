def reverse(x):
    "Given an integer x, return the integer with digits reversed"
    sign = x >= 0
    x = abs(x)
    rev = int("".join(list(reversed(str(x)))))
    return rev if sign else -rev

def reverse_no_string(x):
    "Given an integer x, return the integer with digits reversed without converting to string"
    sign = x >= 0
    x = abs(x)
    digits = []
    while x:
        digits.append(x % 10)
        x = x // 10
    rev = 0
    for i, d in enumerate(reversed(digits)):
        rev += d * (10 ** i)
    return rev if sign else -rev


assert reverse(123) == 321
assert reverse(-123) == -321
assert reverse(1) == 1
assert reverse(-1) == -1
assert reverse(0) == 0

assert reverse_no_string(123) == 321
assert reverse_no_string(-123) == -321
assert reverse_no_string(1) == 1
assert reverse_no_string(-1) == -1
assert reverse_no_string(0) == 0
