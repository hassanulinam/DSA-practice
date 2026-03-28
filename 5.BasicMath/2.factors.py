def get_factors(n: int) -> list[int]:
    factors = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i == i:
                factors.append(i)
            else:
                factors.extend([i, n // i])
    return factors


def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("Enter N: "))
print("Factors:", *get_factors(n))
print("Is Prime:", is_prime(n))
