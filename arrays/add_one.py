def add_one(D):
    """
    Given an integer represented as one digit per entry in an array
    e.g. 123 -> [1, 2, 3]

    Return the integer plus one
    e.g. add_one([1, 2, 3]) = [1, 2, 4]

    """
    D[-1] += 1
    carry = 0
    for i in reversed(range(1, len(D))):
        D[i] += carry
        carry = D[i] // 10
        D[i] %= 10
    D[0] += carry
    if D[0] >= 10:
        D[0] %= 10
        D.insert(0, 1)
    return D

assert add_one([1]) == [2]
assert add_one([0]) == [1]
assert add_one([1, 2, 3]) == [1, 2, 4]
assert add_one([1, 2, 3]) == [1, 2, 4]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
assert add_one([9]) == [1, 0]

