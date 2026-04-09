from typing import Optional

from tree_commons import TreeNode, build_tree


def max_path_sum(root: TreeNode) -> int:
    max_sum = root.val

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        if not node:
            return 0

        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        max_sum = max(max_sum, left + right + node.val)
        return node.val + max(left, right)

    dfs(root)
    return max_sum


# arr = list(map(int, input("Enter arr: ").split()))
arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
tree = build_tree(arr, 0)

if tree:
    print(f"Max path sum: {max_path_sum(tree)}")
