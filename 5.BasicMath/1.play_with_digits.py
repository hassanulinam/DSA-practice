def get_digits_list(n: int) -> list[int]:
    digs = []
    while n > 0:
        d = n % 10
        n //= 10
        digs.append(d)
    return digs


def get_reverse(n: int) -> int:
    rev = 0
    while n > 0:
        digit = n % 10
        n //= 10

        rev = rev * 10 + digit
    return rev


def is_palindrome(n: int) -> bool:
    return get_reverse(n) == n


def is_armstrong(n: int) -> bool:
    digits = get_digits_list(n)
    exp = len(digits)
    s = 0
    for d in digits:
        s += d**exp
    return s == n


n = int(input("Enter N: "))
print("Digits:", get_digits_list(n))
print("Reversed:", get_reverse(n))
print("Is Palindrome:", is_palindrome(n))
print("Is Armstrong:", is_armstrong(n))
