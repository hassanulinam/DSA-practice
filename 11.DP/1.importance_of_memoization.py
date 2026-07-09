memo = {
    0: 0,
    1: 1,
}

recurse_iterations = 0


def fibonacci(n: int) -> int:
    global recurse_iterations
    recurse_iterations += 1
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


def fibonacci_tabulated(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fibonacci_lite(n: int) -> int:
    a, b = 0, 1
    container = 0
    for i in range(2, n + 1):
        container = a + b
        a = b
        b = container
    return container


n = int(input("Enter N:"))
# n = 45
if n < 900:
    print(fibonacci(n))
else:
    print(fibonacci_tabulated(n))
print("LITE VERSION")
print(fibonacci_lite(n))

print("Recursions:", recurse_iterations)
