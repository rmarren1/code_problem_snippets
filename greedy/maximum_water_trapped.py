def max_water_trapped(walls):
    l, r = 0, len(walls) - 1
    most_water = 0
    while l < r:
        most_water = max(most_water, (r - l) * min(walls[l], walls[r]))
        if walls[l] < walls[r]:
            l += 1
        else:
            r -= 1
    return most_water

def main():
    test_cases = [
        [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1],
        [1, 1, 1, 1, 1],
        [100, 100]
    ]
    for walls in test_cases:
        print('Running on input:', walls)
        print('Result:', max_water_trapped(walls))
        print()

main()
