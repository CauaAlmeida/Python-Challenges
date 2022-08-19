from functools import lru_cache

# leibniz formula:
# π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...

n = int(input('Write number'))

@lru_cache(maxsize=None)
def calc_pi(n):

    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1
    pi: float = 0.0

    for n in range (n):
        pi += operation * (numerator/denominator)
        denominator += 2
        operation *= -1
    return pi

print(calc_pi(n))