def isPowerOfN(m: int, n: int) -> bool:
    if m <= 0:
        return False
    if m == 1:
        return True

    if m % n == 0:
        return isPowerOfN(m // n, n)
    return False


M = int(input("Enter M: "))
N = int(input("Enter N: "))
print(f"is m power n: {isPowerOfN(M, N)}")
