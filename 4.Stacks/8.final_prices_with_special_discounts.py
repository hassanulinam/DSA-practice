def get_discounts(prices: list[int]) -> list[int]:
    n = len(prices)
    result = prices.copy()
    stack = []

    for i in range(n):
        while stack and prices[i] <= prices[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] -= prices[i]

        stack.append(i)
    return result


nums = list(map(int, input("Enter prices: ").split()))
print(*get_discounts(nums))
