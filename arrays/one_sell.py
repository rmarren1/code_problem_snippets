def one_sell(A):
    """
    Given A a temporally ordered array of stock prices (left to right),
    return the maximum profit someone could have made buying and selling the stock once.

    """
    max_profit = 0
    min_left = float('inf')

    for i in range(len(A) - 1):
        min_left = min(min_left, A[i])
        profit = A[i + 1] - min_left
        max_profit = max(profit, max_profit)
    return max_profit

assert one_sell([10, 50, 40, 100]) == 90
assert one_sell([0, 100]) == 100
assert one_sell([1000, 100, 10, 0, 1]) == 1
