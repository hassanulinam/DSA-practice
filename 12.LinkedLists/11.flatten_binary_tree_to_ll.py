# https://leetcode.com/problems/flatten-binary-tree-to-linked-list
from typing import Optional

from tree_commons import TreeNode


class Solution:
    def flatten(self, root: Optional["TreeNode"]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(head: Optional["TreeNode"]):
            if not head:
                return None
            left = head.left
            right = head.right
            left_tail = dfs(left)
            right_tail = dfs(right)
            if left:
                head.right = left
                left_tail.right = right
            head.left = None

            return right_tail or left_tail or head

        dfs(root)
