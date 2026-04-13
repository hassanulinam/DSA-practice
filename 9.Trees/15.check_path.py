from typing import Optional

from tree_commons import TreeNode, build_tree


def check_path(root: Optional[TreeNode], path: list[int], i: int) -> bool:
    if not root:
        return False
    if i >= len(path) or root.val != path[i]:
        return False
    if i == len(path) - 1:
        return not root.left and not root.right

    return check_path(root.left, path, i + 1) or check_path(root.right, path, i + 1)


arr = [1, 2, 3, 4, 5, 3]
root = build_tree(arr, 0)
path = [1, 2]
if root:
    print("Does path [1, 2, 5] exist?:", check_path(root, path, 0))
