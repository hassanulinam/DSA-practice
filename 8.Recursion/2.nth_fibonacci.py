def nth_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


n = int(input("Enter N: "))
print(nth_fibonacci(n))
