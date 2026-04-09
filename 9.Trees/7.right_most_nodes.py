from typing import Optional

from tree_commons import TreeNode, build_tree


def rhs(root: TreeNode) -> list[str]:
    ans = []

    def dfs(node: Optional[TreeNode], level: int) -> None:
        if not node:
            return
        if level == len(ans):
            ans.append(node.val)

        dfs(node.right, level + 1)
        dfs(node.left, level + 1)

    dfs(root, 0)
    return ans


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tree = build_tree(arr, 0)
if tree:
    print("Right side view:", rhs(tree))
