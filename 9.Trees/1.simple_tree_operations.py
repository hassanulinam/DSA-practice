from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def build_tree(arr: list[int], i: int) -> Optional[TreeNode]:
    if i >= len(arr) or arr[i] is None:
        return None

    root = TreeNode(arr[i])

    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)

    return root


def pre_order(tree: TreeNode) -> list[int]:
    result = []

    def traverse(node: Optional[TreeNode]) -> None:
        if not node:
            return

        result.append(node.val)
        traverse(node.left)
        traverse(node.right)

    traverse(tree)
    return result


def in_order(tree: TreeNode) -> list[int]:
    result: list[int] = []

    def traverse(node: Optional[TreeNode]) -> None:
        if not node:
            return

        traverse(node.left)
        result.append(node.val)
        traverse(node.right)

    traverse(tree)
    return result


def post_order(tree: TreeNode) -> list[int]:
    result: list[int] = []

    def traverse(node: Optional[TreeNode]) -> None:
        if not node:
            return

        traverse(node.left)
        traverse(node.right)
        result.append(node.val)

    traverse(tree)
    return result


def max_depth(node: Optional[TreeNode]) -> int:
    if not node:
        return 0

    return 1 + max(max_depth(node.left), max_depth(node.right))


def bfs(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    result: list[int] = []

    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result


def level_order_bfs(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []

    result: list[list[int]] = []
    q = deque([root])

    while q:
        level = []
        size = len(q)

        for i in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level)
    return result


def is_same_tree(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    if root1.val != root2.val:
        return False

    return is_same_tree(root1.left, root2.left) and is_same_tree(
        root1.right, root2.right
    )


def invert_tree_bottom_up(node: Optional[TreeNode]) -> Optional[TreeNode]:
    if not node:
        return None

    inverted_right = invert_tree_bottom_up(node.right)
    inverted_left = invert_tree_bottom_up(node.left)

    node.left = inverted_right
    node.right = inverted_left
    return node


def invert_tree_top_down(node: Optional[TreeNode]) -> None:
    if not node:
        return

    node.left, node.right = node.right, node.left
    invert_tree_top_down(node.left)
    invert_tree_top_down(node.right)


def __main__():
    # arr = list(map(int, input("Enter nums to build tree: ").split()))
    nums_len = int(input("Enter the range limit: "))
    arr = list(range(nums_len))
    tree = build_tree(arr, 0)

    if tree:
        # print("Pre Order:", pre_order(tree))
        # print("In Order:", in_order(tree))
        # print("Post Order:", post_order(tree))
        # print(f"Input_Length -> {len(arr)},  max_depth -> {max_depth(tree)}")
        # print(f"BFS traversal: {bfs(tree)}")
        print(f"Level Order BFS: {level_order_bfs(tree)}")

        print(f"Is Same?: {is_same_tree(tree, tree)}")
        print(f"Is Same?: {is_same_tree(tree.left, tree.right)}")

        print("Bottom-up inversion:", level_order_bfs(invert_tree_bottom_up(tree)))

        invert_tree_top_down(tree)
        print("Top-down inversion:", level_order_bfs(tree))


__main__()
