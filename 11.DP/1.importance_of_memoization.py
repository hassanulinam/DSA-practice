memo = {
    0: 0,
    1: 1,
}


def fibonacci(n: int) -> int:
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]


# for n = 40, it took 8 secs., and for n = 45 it took around 1min 40secs.
def fibonacci_raw(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_raw(n - 1) + fibonacci_raw(n - 2)


n = int(input("Enter N:"))
# n = 45
print(fibonacci(n))
