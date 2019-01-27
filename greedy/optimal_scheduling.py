"""
Given 2n tasks with a positive integral task duration for each task,
return an optimal scheduling of these tasks onto n workers such that
each worker does exactly two tasks, and the duration of the slowest worker
is minimal.

"""
def optimal_scheduling(tasks):
    tasks.sort()
    return [(tasks[i], tasks[~i]) for i in range(len(tasks) // 2)]

def main():
    test_cases = [
            [1, 2, 3, 4],
            [1, 2, 1, 2],
            [1, 1, 1, 1],
            [],
            [100, 1000, 100000, 1e9],
            [2, 2, 2, 2, 3, 3, 3, 3]
    ]
    for tasks in test_cases:
        print('Running on tasks:', tasks)
        output = optimal_scheduling(tasks)
        print('Output:', output)
        print()

main()

