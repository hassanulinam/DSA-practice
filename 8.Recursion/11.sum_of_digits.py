def sum_of_digits(n: int) -> int:
    if n <= 0:
        return n

    return n % 10 + sum_of_digits(n // 10)


def get_number_reversed(acc: int, n: int) -> int:
    if n <= 0:
        return acc
    acc = acc * 10 + n % 10
    return get_number_reversed(acc, n // 10)


def get_rev_with_loop(n: int) -> int:
    rev = 0
    while n > 0:
        last_dig = n % 10
        rev = rev * 10 + last_dig
        n //= 10
    return rev


n = int(input("Enter N: "))
print(sum_of_digits(n))
print(f"Reversed: {get_number_reversed(0, n)}")
