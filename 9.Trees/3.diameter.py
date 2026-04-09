from typing import Optional

from tree_commons import TreeNode, build_tree


def diameter(root: TreeNode) -> int:
    dm = 0

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal dm
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)
        dm = max(dm, left + right)
        return 1 + max(left, right)

    dfs(root)
    return dm


def __main__():
    nums_len = int(input("Enter the range limit: "))
    arr = list(range(nums_len))
    tree = build_tree(arr, 0)

    if tree:
        print("Diameter:", diameter(tree))


__main__()
