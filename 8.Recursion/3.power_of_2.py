# https://leetcode.com/problems/power-of-two


def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False

    if n == 1:
        return True

    if n % 2 == 0:
        return isPowerOfTwo(n // 2)
    return False


def isPowerOfTwoByBitManipulation(n: int) -> bool:
    return (n > 0) and not (n & n - 1)


N = int(input("Enter N: "))
print(f"{N} is power of 2: {isPowerOfTwo(N)}")
print(f"{N} is power of 2: {isPowerOfTwoByBitManipulation(N)}")
