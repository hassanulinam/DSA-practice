# https://leetcode.com/problems/generate-parentheses


def generate_paranthesis(n: int, out: list[str]) -> list[str]:
    if n == 0:
        return []

    if n == 1:
        out.append("()")
        return out

    out.append(("(" * n + ")" * n))
    p1 = generate_paranthesis(n - 1, [])
    for k in p1:
        out.append("()" + k)
        # if k != "()":
        out.append(k + "()")

    return list(set(out))


n = int(input("Enter N: "))
print(generate_paranthesis(n, []))
