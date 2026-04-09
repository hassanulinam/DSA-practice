"""
🧩 Count Good Nodes in Binary Tree
A node is called “good” if - No node on the path from root → that node has a value greater than it
"""

from typing import Optional

from tree_commons import TreeNode, build_tree


def no_of_good_nodes(node: Optional[TreeNode], pivot: int) -> int:
    if not node:
        return 0

    current = 0
    if node.val >= pivot:
        current = 1
        pivot = node.val

    left = no_of_good_nodes(node.left, pivot)
    right = no_of_good_nodes(node.right, pivot)

    return current + left + right


def __main__():
    arr = [5, 4, 6, 3]
    tree = build_tree(arr, 0)
    if tree:
        print("No Of Good Nodes:", no_of_good_nodes(tree, tree.val))


__main__()
