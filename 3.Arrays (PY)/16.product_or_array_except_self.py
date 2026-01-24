# https://leetcode.com/problems/product-of-array-except-self


def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)

    prefix = 1
    ans = [1]

    for i in range(1, n):
        prefix *= nums[i - 1]
        ans.append(prefix)

    suffix = 1
    for i in range(n - 2, -1, -1):
        suffix *= nums[i + 1]
        ans[i] *= suffix

    return ans


print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf([-1, 1, 0, -3, 3]))
