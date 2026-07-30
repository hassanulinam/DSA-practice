# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
from tree_commons import TreeNode, print_tree


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        n = len(nums)

        def dfs(l: int, r: int):
            if l > r:
                return None
            mid = (l + r) >> 1
            head = TreeNode(nums[mid])
            head.left = dfs(l, mid - 1)
            head.right = dfs(mid + 1, r)
            return head

        return dfs(0, n - 1)


arr = list(map(int, input("Enter sorted arr: ").split()))
print_tree(Solution().sortedArrayToBST(arr))
