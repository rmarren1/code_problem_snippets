"""
Given a set of intervals i1, i2, ..., in

Find the smallest set of points p1, p2, ..., pk

Such that each interval is covered by some point

"""
def minimal_set_cover(intervals):
    intervals.sort(key=lambda x: x[1])
    chosen = []
    for l, r in intervals:
        if not chosen or chosen and not (l <= chosen[-1] <= r):
            chosen.append(r)
    return len(chosen)

def main():
    test_cases = [
        [(2, 3), (4, 5), (2, 3), (5, 6), (1, 2)],
        [(1, 2), (1, 2), (1, 2), (1, 4)],
        []
    ]
    for intervals in test_cases:
        print("Computing for intervals:", intervals)
        print("Result:", minimal_set_cover(intervals))
        print()

main()
