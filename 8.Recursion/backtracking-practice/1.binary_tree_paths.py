# https://leetcode.com/problems/binary-tree-paths?envType=problem-list-v2&envId=backtracking
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        result: list[str] = []

        if not root:
            return []

        def backtrack(node: TreeNode, path: list[int]) -> None:
            path.append(node.val)

            if not node.left and not node.right:
                s = "->".join(map(str, path))
                result.append(s)
            else:
                if node.left:
                    backtrack(node.left, path)
                if node.right:
                    backtrack(node.right, path)
            path.pop()

        backtrack(root, [])
        return result


# def __main__():
#     arr = list(map(int, input("Enter arr: ").split()))
