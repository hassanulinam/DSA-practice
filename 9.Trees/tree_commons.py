from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def build_tree(arr, i: int) -> Optional[TreeNode]:
    if i >= len(arr) or arr[i] is None:
        return None

    root = TreeNode(arr[i])

    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)

    return root
