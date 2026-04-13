from collections import deque

from tree_commons import TreeNode, build_tree


def zigzag_level_order(root: TreeNode) -> list[list[int]]:
    result: list[list[int]] = []
    q = deque([root])
    left_to_right = True

    path: deque[int] = deque()
    while q:
        size = len(q)

        for i in range(size):
            node = q.popleft()
            if left_to_right:
                path.append(node.val)
            else:
                path.appendleft(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.app(list(path))
        path.clear()
        left_to_right = not left_to_right

    return result


arr = [1, 2, 3, 4, 5, None, 6]
tree = build_tree(arr, 0)
if tree:
    print("Zig Zag Level Order:", zigzag_level_order(tree))
