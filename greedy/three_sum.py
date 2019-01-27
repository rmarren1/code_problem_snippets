def three_sum(nums, target):
    nums.sort()
    for i in range(len(nums)):
        l, r = i, len(nums) - 1
        while l <= r:
            curr = [nums[i], nums[l], nums[r]]
            s = sum(curr)
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:  # s == target
                return curr
    return None

def main():
    test_cases = [
        ([1], 3),
        ([2, 4, 5], 12),
        ([-1, -1, 2], 0)
    ]
    for nums, target in test_cases:
        print('Running on params', nums, target)
        print('Result:', three_sum(nums, target))
        print()
main()
