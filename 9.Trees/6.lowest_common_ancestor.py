from typing import Optional

from tree_commons import TreeNode, build_tree


def lca(root: Optional[TreeNode], N1: int, N2: int) -> Optional[TreeNode]:
    if not root:
        return None
    left = lca(root.left, N1, N2)
    right = lca(root.right, N1, N2)

    if left and right:
        return root

    if root.val == N1 or root.val == N2:
        return root

    return left or right


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
a, b = list(map(int, input("Enter A, B: ").split()))
tree = build_tree(arr, 0)
if tree:
    lca_node = lca(tree, a, b)
    if lca_node:
        print("LCA:", lca_node.val)
    else:
        print("LCA not found")
