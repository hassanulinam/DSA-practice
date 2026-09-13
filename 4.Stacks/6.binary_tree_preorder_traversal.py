# https://leetcode.com/problems/binary-tree-inorder-traversal

from typing import Optional

from tree_commons import TreeNode, build_tree, print_tree


class RecursiveSolution:
    def preorder(self, root: Optional["TreeNode"]) -> list[int]:
        result = []

        def dfs(node: Optional["TreeNode"]):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result

    def inorder(self, root: Optional["TreeNode"]) -> list[int]:
        result = []

        def dfs(node: Optional["TreeNode"]):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result

    def postorder(self, root: Optional["TreeNode"]) -> list[int]:
        result = []

        def dfs(node: Optional["TreeNode"]):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result


class StackSolution:
    def preorder(self, root: TreeNode) -> list[int]:
        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def inorder(self, root: TreeNode) -> list[int]:
        stack: list[TreeNode] = []
        result: list[int] = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result

    def postorder(self, root: TreeNode) -> list[int]:
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]


arr = list(map(int, input("Enter tree nodes: ").split()))
root = build_tree(arr, 0)
print("Given Tree: ")
print_tree(root)
print("\n----")

recur = RecursiveSolution()
stack = StackSolution()
if root:
    print(*stack.postorder(root))
    print(*recur.postorder(root))
