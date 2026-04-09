from typing import Optional

from tree_commons import TreeNode, build_tree


def is_balanced_tree(root: TreeNode) -> bool:

    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return False

        left = dfs(node.left)
        if left == -1:
            return -1

        right = dfs(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return dfs(root) != -1


def __main__():
    nums_len = int(input("Enter the range limit: "))
    arr = list(range(nums_len))
    tree = build_tree(arr, 0)

    if tree:
        print("Is Balanced:", is_balanced_tree(tree))


__main__()
