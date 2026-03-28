def generate_paranthesis(n: int) -> list[str]:
    result: list[str] = []

    def backtrack(S: str, open: int, close: int) -> None:
        if len(S) == 2 * n:
            result.append(S)
            return

        if open < n:
            backtrack(S + "(", open + 1, close)
        if close < open:
            backtrack(S + ")", open, close + 1)

    backtrack("", 0, 0)

    return result


n = int(input("Enter N: "))
print(generate_paranthesis(n))
