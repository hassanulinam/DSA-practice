class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / (x * self.myPow(x, (-n - 1)))

        half_exp = self.myPow(x, n // 2)
        coeff = 1 if (n % 2 == 0) else x
        return coeff * half_exp * half_exp


sol = Solution()
print(sol.myPow(2, 10))
print(sol.myPow(2, -2))
