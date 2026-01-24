def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1
    p2 = n - 1
    i = m + n - 1

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            p1 -= 1
        else:
            nums1[i] = nums2[p2]
            p2 -= 1
        i -= 1


arr = [4, 5, 6, 0, 0, 0]
merge(arr, 3, [1, 2, 3], 3)
print(arr)
