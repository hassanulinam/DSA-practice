def sum_of_digits(n: int) -> int:
    if n < 0:
        return n
    if n // 10 == 0:
        return n

    return n % 10 + sum_of_digits(n // 10)


n = int(input("Enter N: "))
print(sum_of_digits(n))
