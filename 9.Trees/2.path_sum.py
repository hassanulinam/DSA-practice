from typing import Optional

from tree_commons import TreeNode, build_tree


def path_sum(root: Optional[TreeNode], target: int) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        return target == root.val

    remaining = target - root.val
    return path_sum(root.left, remaining) or path_sum(root.right, remaining)


def get_a_single_sum_path(root: TreeNode, target: int) -> list[int]:
    path: list[int] = []

    def dfs(node: Optional[TreeNode], remaining: int) -> bool:
        if not node:
            return False

        path.append(node.val)
        remaining -= node.val

        if not node.left and not node.right and remaining == 0:
            return True

        if dfs(node.left, remaining) or dfs(node.right, remaining):
            return True

        path.pop()
        return False

    if dfs(root, target):
        return path
    return []


def get_all_sum_paths(root: TreeNode, target: int) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def dfs(node: Optional[TreeNode], remaining: int) -> None:
        if not node:
            return

        path.append(node.val)
        remaining -= node.val
        if not node.left and not node.right and remaining == 0:
            result.append(path[:])
            return

        dfs(node.left, remaining)
        dfs(node.right, remaining)
        path.pop()

    dfs(root, target)
    return result


def __main__():
    # arr = list(map(int, input("Enter nums to build tree: ").split()))
    nums_len = int(input("Enter the range limit: "))
    arr = list(range(nums_len))
    target_sum = int(input("Enter target sum: "))
    tree = build_tree(arr, 0)

    if tree:
        print("Is path_sum there?:", get_a_single_sum_path(tree, target_sum))
        print("All sum Paths:", get_all_sum_paths(tree, target_sum))


__main__()
