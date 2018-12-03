import random
from collections import defaultdict

def _random():
    return random.random() > 0.5

def random_six():
    """
    Create a RNG which selects the numbers 0, 1, 2, 3, 4, 5 evenly,
    given only an unbiased coin.
    """
    rand = _random() + (_random() << 1) + (_random() << 2)
    if rand <= 5:
        return rand
    return random_six()

print("Running 1 million iterations, will print results in a few seconds")
results = defaultdict(lambda: 0)
for _ in range(int(10e6)):
    results[random_six()] += 1
print(dict(results))

