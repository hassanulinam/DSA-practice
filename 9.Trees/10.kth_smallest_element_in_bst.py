from typing import Optional

from tree_commons import TreeNode, build_tree


def inorder_list(root: TreeNode) -> list[int]:
    result = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


def kth_smallest(root: TreeNode, k: int) -> Optional[TreeNode]:
    ans = None
    ground_level = 0

    def dfs(node: Optional[TreeNode]) -> None:
        nonlocal ans, ground_level
        if not node or ans:
            return

        dfs(node.left)
        ground_level += 1
        if ground_level == k:
            ans = node
            return
        dfs(node.right)

    dfs(root)
    return ans


arr = [5, 3, 6, 2, 4, None, None, 1]
tree = build_tree(arr, 0)
k = int(input("Enter k: "))
if tree:
    print("In order:", inorder_list(tree))
    ans = kth_smallest(tree, k)
    if ans:
        print(f"{k}th smallest: {ans.val}")
    else:
        print("Not found")


"""
## 🧩 **Kth Smallest Element in a BST**

---

## 📌 Problem

Given a **BST**, return the **k-th smallest element**

---

## 🧠 Key property of BST

```text
Inorder traversal → sorted order
```

---

## 🔍 Example 1

```text
        3
       / \
      1   4
       \
        2
```

```text
k = 1 → 1
k = 2 → 2
k = 3 → 3
k = 4 → 4
```

---

## 🔍 Example 2

```text
        5
       / \
      3   6
     / \
    2   4
   /
  1
```

```text
k = 3 → 3
```

---

## ⚠️ Constraints

* 1 ≤ k ≤ number of nodes
* Must be efficient (don’t store full array unless needed)

---

## 🧪 Edge Case

```text
Single node → k=1 → return root
```

---

Take your time.

This one will test:

* traversal control
* stopping recursion early

---

Send your attempt when ready.

"""
