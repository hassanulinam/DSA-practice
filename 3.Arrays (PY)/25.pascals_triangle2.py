class Solution:
    def generate(self, rowIndex: int) -> list[int]:
        prev_row = []
        for i in range(rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = prev_row[j - 1] + prev_row[j]
            prev_row = row
        return prev_row


n = int(input("Enter n: "))
sol = Solution().generate(n)
print(*sol)
