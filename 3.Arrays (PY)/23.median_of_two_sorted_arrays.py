class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i, j = 0, 0
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged += nums1[i:]
        merged += nums2[j:]
        n = len(merged)
        mid_index = n // 2
        if n % 2:
            return merged[mid_index]
        return (merged[mid_index] + merged[mid_index - 1]) / 2
