def one_sell(A):
    """
    Given A a temporally ordered array of stock prices (left to right),
    return the maximum profit someone could have made buying and selling the stock once.

    This solution is O(n^2)
    There is a O(n) solution.

    """
    max_profit = 0
    min_left = float('inf')

    for i in range(len(A) - 1):
        min_left = min(min_left, A[i])
        profit = A[i + 1] - min_left
        max_profit = max(profit, max_profit)
    return max_profit

def two_sell(A):
    max_profit = 0
    for i in range(2, len(A) - 1):
        max_profit = max(max_profit, one_sell(A[:i]) + one_sell(A[i:]))
    print(max_profit)
    return max_profit

assert two_sell([10, 50, 40, 100]) == 100
assert two_sell([0, 100, 10, 11]) == 101
assert two_sell([0, 10, 70, 10, 70, 100]) == 160
