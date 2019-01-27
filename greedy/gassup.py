def gasup(gasses, distance_to_next):
    MPG = 20
    gas = 0
    min_gas = 0
    lowest_city = 0
    for i, (g, d) in enumerate(zip(gasses, distance_to_next)):
        if gas < min_gas:
            min_gas = gas
            lowest_city = i
        gas += g
        gas -= d // MPG
    return lowest_city

def main():
    test_cases = [
       ([50, 20, 5, 30, 25, 10, 10], [900, 600, 200, 400, 600, 200, 100])
    ]
    for gasses, distance_to_next in test_cases:
        print('Running on:', gasses, distance_to_next)
        print('Result:', gasup(gasses, distance_to_next))
        print()

main()
