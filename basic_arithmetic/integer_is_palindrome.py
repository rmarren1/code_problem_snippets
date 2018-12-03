import math

def check_palindrome(x):
    """
    return True if the string representation of x is a palindrome
    return False otherwise

    Time complexity - O(n)
    Space complexity - O(n)
    where n is the number of digits in x
    """
    # If x is negative, its representation starts with a '-'
    # so it can't be a palindrome
    # since an integer will never end with a '-'
    if x < 0:
        return False
    digits = str(x)
    for i in range(len(digits) // 2):
        if digits[i] != digits[-i - 1]:
            return False
    return True

def check_palindrome_no_string(x):
    """
    return True if the string representation of x is a palindrome
    return False otherwise
    Do not convert to a string

    Time complexity - O(n)
    Space complexity - O(1)
    where n is the number of digits in x
    """
    def _extract_digit(x, i):
        return (x // 10**(i)) % 10

    # If x is negative, its representation starts with a '-'
    # so it can't be a palindrome
    # since an integer will never end with a '-'
    if x < 0:
        return False
    # Need this check since math.log(0) is undefined
    if x == 0:
        return True
    n = int(math.floor(math.log(x, 10)) + 1)
    for i in range(n // 2):
        if  _extract_digit(x, i) != _extract_digit(x, n - i - 1):
            return False
    return True


assert     check_palindrome(0)
assert     check_palindrome(1)
assert not check_palindrome(-1)
assert     check_palindrome(11)
assert     check_palindrome(121)
assert not check_palindrome(-121)
assert     check_palindrome(12321)
assert     check_palindrome(12345678987654321)
assert not check_palindrome(123432)

assert     check_palindrome_no_string(0)
assert     check_palindrome_no_string(1)
assert not check_palindrome_no_string(-1)
assert     check_palindrome_no_string(11)
assert     check_palindrome_no_string(121)
assert not check_palindrome_no_string(-121)
assert     check_palindrome_no_string(12321)
assert     check_palindrome_no_string(12345678987654321)
assert not check_palindrome_no_string(123432)

