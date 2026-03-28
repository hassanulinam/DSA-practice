# https://leetcode.com/problems/time-based-key-value-store


class TimeMap:
    def __init__(self):
        self.mp = dict()

    def set(self, key: str, value: str, ts: int) -> None:
        if key in self.mp:
            self.mp[key].append([value, ts])
        else:
            self.mp.__setitem__(key, [[value, ts]])

    def get(self, key: str, ts: int) -> str:
        if key not in self.mp:
            return ""
        space = self.mp[key]
        left, right = 0, len(space) - 1
        result = ""
        while left <= right:
            mid = (right + left) // 2

            if space[mid][1] <= ts:
                result = space[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result
