# GCD - Greatest Common Divisor == HCF - Highest Common Factor
def gcd(a: int, b: int) -> int:
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a

    return max(a, b)


nums = [int(x) for x in input().split()]
print("GCD of", nums[0], "and", nums[1], "=", gcd(nums[0], nums[1]))
