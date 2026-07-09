"""https://leetcode.com/problems/climbing-stairs
🧗 Climbing Stairs
You are climbing a staircase.
It takes n steps to reach the top.
Each time, you can climb either:
* 1 step
* 2 steps
Return the number of distinct ways to reach the top.
"""

memo = {0: 0, 1: 1, 2: 2}


def get_no_of_ways(n: int) -> int:
    if n in memo:
        return memo[n]
    memo[n] = get_no_of_ways(n - 1) + get_no_of_ways(n - 2)
    return memo[n]


def get_nways_tabulated(n: int) -> int:
    if n < 3:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def get_nways_optimal(n: int) -> int:
    if n < 3:
        return n

    a, b = 1, 2
    for i in range(3, n + 1):
        curr = a + b
        a, b = b, curr
    return b


n = int(input("Enter N: "))
print(get_no_of_ways(n))
print(get_nways_tabulated(n))
print(get_nways_optimal(n))
