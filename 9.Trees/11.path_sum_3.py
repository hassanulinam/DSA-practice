from collections import deque
from typing import Optional

from tree_commons import TreeNode, build_tree


def level_order_bfs(root: TreeNode) -> list[list[int]]:
    result: list[list[int]] = []
    q = deque([root])
    while q:
        path: list[int] = []
        size = len(q)
        for i in range(size):
            node = q.popleft()
            path.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(path[:])
    return result


def path_sum_3(root: TreeNode, target: int) -> int:
    total = 0
    sum_freqs = {0: 1}

    def dfs(node: Optional[TreeNode], current_sum: int):
        nonlocal total
        if not node:
            return
        current_sum += node.val
        total += sum_freqs.get(current_sum - target, 0)

        csum_freq = sum_freqs.get(current_sum, 0)
        sum_freqs[current_sum] = csum_freq + 1

        dfs(node.left, current_sum)
        dfs(node.right, current_sum)
        sum_freqs[current_sum] -= 1

    dfs(root, 0)
    return total


arr = [10, 5, -3, 3, 2, 11, None, 3, -2, 1]
tree = build_tree(arr, 0)
if tree:
    print("Level order BFS:", level_order_bfs(tree))
    print("Path sum:", path_sum_3(tree, 8))


"""
## 🔥 Next Problem: Path Sum III

### Problem

Given the root of a binary tree and an integer `targetSum`, return the **number of paths** where the sum of the values equals `targetSum`.

👉 Important constraints:

* The path **does NOT need to start at root**
* The path **does NOT need to end at a leaf**
* But it must go **downward (parent → child only)**

---

### Example

```
       10
      /  \
     5   -3
    / \    \
   3   2    11
  / \   \
 3  -2   1

targetSum = 8
```

Valid paths:

* 5 → 3
* 5 → 2 → 1
* -3 → 11

Answer = 3

---

## 🧠 Why this is perfect for you

This problem will break your current mental model in a good way:

You’ve mostly done:

* root → leaf paths
* single path tracking

This forces you to understand:

* **Every node can be a starting point**
* You need **nested DFS thinking**
* Or optimize using prefix sums (advanced)

---

## ⚠️ Common mistakes (you WILL hit these)

* Trying to track only one running sum → ❌ wrong
* Forgetting to restart path at every node → ❌ wrong
* Mixing up “path” vs “subtree” → ❌ very common

---

## 💡 Your task (don’t skip this)

1. First try a brute force approach:

   * For every node → start a DFS
   * Count valid paths

2. Once you get that working:

   * Optimize it (hint: prefix sum)

---

## 🎯 What I expect from you

Come back with:

* Your brute force solution
* Where you got stuck (if any)
* Your thought process (this matters more than code)

---

If this feels “confusing”, that’s exactly the point — this is the level where real tree intuition starts forming.

"""
