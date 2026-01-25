# https://leetcode.com/problems/valid-parentheses
def isValid(s: str) -> bool:
    strmap = {"(": ")", "[": "]", "{": "}"}
    stack = []

    if len(s) % 2 != 0:
        return False

    for c in s:
        if c in strmap:
            stack.append(strmap[c])
        else:
            if not stack or c != stack[-1]:
                return False
            stack.pop()

    return not stack


inputs = ["()", "()[]{}", "([])", "([)]", "(){}}{", "(((]", "({}[](("]
for x in inputs:
    print(x, "\t:", isValid(x))
