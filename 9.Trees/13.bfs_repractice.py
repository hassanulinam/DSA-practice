from collections import deque
from typing import Optional

from tree_commons import TreeNode, build_tree


def level_order(root: TreeNode) -> list[list[int]]:
    result: list[list[int]] = []
    q = deque([root])
    while q:
        path = []
        size = len(q)
        for i in range(size):
            node = q.popleft()
            path.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(path)
    return result


def zigzag_level_order(root: TreeNode) -> list[list[int]]:
    result: list[list[int]] = []
    ltr = True
    q = deque([root])
    path: deque[int] = deque()
    while q:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            if ltr:
                path.append(node.val)
            else:
                path.appendleft(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(list(path))
        ltr = not ltr
        path.clear()
    return result


def right_side_view(root: TreeNode) -> list[int]:
    result: list[int] = []

    def dfs(node: Optional[TreeNode], level: int) -> None:
        if not node:
            return

        if len(result) == level:
            result.append(node.val)

        dfs(node.right, level + 1)
        dfs(node.left, level + 1)

    dfs(root, 0)
    return result


def right_side_view_bfs(tree: TreeNode) -> list[int]:
    result: list[int] = []
    q = deque([tree])

    rightmost = tree.val
    while q:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            rightmost = node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(rightmost)

    return result


def average_of_levels(root: TreeNode) -> list[float]:
    result: list[float] = []
    q = deque([root])
    while q:
        level_sum = 0
        size = len(q)
        for i in range(size):
            node = q.popleft()
            level_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level_sum / size)
    return result


def minimum_depth_bfs(root: TreeNode) -> int:
    if not root:
        return 0
    depth = 0
    q = deque([root])
    while q:
        size = len(q)
        depth += 1
        for _ in range(size):
            node = q.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return depth


arr = [1, 2, 3, 4, 5, 6]
root = build_tree(arr, 0)
if root:
    print("Level Order:", level_order(root))
    print("ZigZag level order:", zigzag_level_order(root))
    print("Right side view:", right_side_view(root))
    print("Right side view:", right_side_view_bfs(root))
    print("Average of levels:", average_of_levels(root))
    print("Min Depth:", minimum_depth_bfs(root))
