from typing import Optional

from tree_commons import TreeNode, build_tree


def binary_tree_paths(root: TreeNode) -> list[str]:
    result: list[str] = []

    def dfs(node: Optional[TreeNode], path: list[int]) -> None:
        if not node:
            return

        path.append(node.val)
        if not node.left and not node.right:
            tree_path = "->".join(list(map(str, path)))
            result.append(tree_path)
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()

    dfs(root, [])
    return result


def path_sum2(root: TreeNode, target: int) -> list[list[int]]:
    result = []

    def dfs(node: Optional[TreeNode], remaining: int, path: list[int]) -> None:
        if not node:
            return

        path.append(node.val)
        remaining -= node.val
        if not node.left and not node.right and remaining == 0:
            result.append(path[:])
        else:
            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)
        path.pop()

    dfs(root, target, [])
    return result


def path_sum3(root: TreeNode, target: int) -> int:
    cnt = 0
    sum_freqs = {0: 1}

    def dfs(node: Optional[TreeNode], current_sum: int) -> None:
        nonlocal cnt
        if not node:
            return

        current_sum += node.val
        prev_sum = target - current_sum
        cnt += sum_freqs.get(prev_sum, 0)
        sum_freqs[current_sum] = sum_freqs.get(current_sum, 0) + 1
        dfs(node.left, current_sum)
        dfs(node.right, current_sum)
        sum_freqs[current_sum] -= 1

    dfs(root, 0)
    return cnt


def LCA(root: Optional[TreeNode], N1: int, N2: int) -> Optional[TreeNode]:
    if not root:
        return None

    if root.val == N1 or root.val == N2:
        return root

    left = LCA(root.left, N1, N2)
    right = LCA(root.right, N1, N2)

    if left and right:
        return root

    return left or right


arr = [1, 2, 3, 4, 5, 3]
root = build_tree(arr, 0)
if root:
    print("Binary Paths:", binary_tree_paths(root))
    print("Sum Paths:", path_sum2(root, 7))
