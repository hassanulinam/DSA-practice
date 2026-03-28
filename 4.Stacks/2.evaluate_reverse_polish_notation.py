# https://leetcode.com/problems/evaluate-reverse-polish-notation
def evaluateExpression(left: int, right: int, operator: str) -> int:
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    return int(left / right)


def evalRPN(tokens: list[str]) -> int:
    symbols = {"+", "-", "/", "*"}
    stack: list[int] = []

    for t in tokens:
        if t in symbols:
            right = stack.pop()
            left = stack.pop()
            evaluated_value = evaluateExpression(left, right, t)
            stack.append(evaluated_value)
        else:
            stack.append(int(t))

    return stack[0]


inputs = [
    ["2", "1", "+", "3", "*"],
    ["4", "13", "5", "/", "+"],
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
]

for x in inputs:
    print(evalRPN(x))
