# remove k digits to make the number smallest as possible
# IDEA: just remove the bigger numbers before smaller numbers. Use monotonic increasing stack


def make_smaller(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # safeguard incase the above loop (elimination) hasn't executed.
    while k > 0:
        stack.pop()
        k -= 1

    result = "".join(stack).lstrip("0")
    return result if result else "0"


num = input("Enter Num: ")
k = int(input("Enter k: "))
print(make_smaller(num, k))
