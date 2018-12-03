def check_palindrome(x):
    """
    return True if the string representation of x is a palindrome
    return False otherwise
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

assert check_palindrome(0)
assert check_palindrome(1)
assert not check_palindrome(-1)
assert check_palindrome(11)
assert check_palindrome(121)
assert not check_palindrome(-121)
assert check_palindrome(12321)
assert check_palindrome(12345678987654321)
assert not check_palindrome(123432)

