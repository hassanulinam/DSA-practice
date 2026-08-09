# https://leetcode.com/problems/next-greater-element-i
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        idx_map = {}
        for i in range(len(nums2)):
            idx_map[nums2[i]] = i

        result = []
        for i in range(len(nums1)):
            k = nums1[i]
            found = False
            for j in range(idx_map[nums1[i]], len(nums2)):
                if nums2[j] > k:
                    result.append(nums2[j])
                    found = True
                    break
            if not found:
                result.append(-1)
        return result

    def monotonicApproach(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = [0]
        greater_map = {}
        for i in range(1, len(nums2)):
            k = nums2[i]
            while stack and nums2[stack[-1]] < k:
                greater_map[nums2[stack.pop()]] = k
            stack.append(i)
            i += 1

        result = [greater_map.get(x, -1) for x in nums1]
        return result


arr = list(map(int, input("Enter nums1: ").split()))
arr2 = list(map(int, input("Enter nums2: ").split()))
sol = Solution()
print(*sol.nextGreaterElement(arr, arr2))
print(*sol.monotonicApproach(arr, arr2))
