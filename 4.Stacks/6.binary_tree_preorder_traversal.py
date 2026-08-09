# https://leetcode.com/problems/binary-tree-inorder-traversal

from typing import Optional

from tree_commons import TreeNode, build_tree


class Solution:
    def preorderTraversal(self, root: Optional["TreeNode"]) -> list[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def recursivePreOrder(self, root: Optional["TreeNode"]) -> list[int]:
        result = []

        def dfs(node: Optional["TreeNode"]):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result

    def inorderTraversal(self, root: Optional["TreeNode"]) -> list[int]:
        if not root:
            return []
        node, stack, output = root, [], []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            output.append(node.val)
            node = node.right
        return output

    def recursiveInOrder(self, root: Optional["TreeNode"]) -> list[int]:
        result = []

        def dfs(node: Optional["TreeNode"]):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result

    def postorderTraversal(self, root: Optional["TreeNode"]) -> list[int]:
        if not root:
            return []
        stack, output = [root], []
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return output[::-1]

    def recursivePostOrder(self, root: Optional["TreeNode"]) -> list[int]:
        result = []

        def dfs(node: Optional["TreeNode"]):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result


arr = list(map(int, input("Enter tree nodes: ").split()))
root = build_tree(arr, 0)
sol = Solution()
print(*sol.postorderTraversal(root))
print(*sol.recursivePostOrder(root))
