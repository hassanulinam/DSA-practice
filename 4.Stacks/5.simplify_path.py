# https://leetcode.com/problems/simplify-path


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack: list[str] = []
        n = len(path)
        i = 0
        while i < n:
            while i < n and path[i] == "/":
                i += 1
            j = i
            while j < n and path[j] != "/":
                j += 1

            dir = path[i:j]
            if dir in (".", "/"):
                pass
            elif dir == "..":
                if stack:
                    stack.pop()
            elif dir:
                stack.append(dir)
            i = j

        return "/" + "/".join(stack)


path = input("Enter path: ")
print(Solution().simplifyPath(path))
