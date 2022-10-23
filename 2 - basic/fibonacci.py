from functools import lru_cache

# fib(n) = fib(n-1) + fib(n-2)
# fib(0) = 0
# fib(1) = 1
# fib(2) = 1
# ...

# INPUT THE RANGE OF THE ANALYSIS
n = int(input('Write the range: '))


# LEAST RECENTLY USED CACHE
# 

@lru_cache(maxsize=1000)
def fib(x):
    if x in {0, 1}:
        return x
    return fib(x - 1) + fib(x - 2)


print([fib(n) for n in range(n)])
