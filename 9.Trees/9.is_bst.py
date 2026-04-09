from typing import Optional

from tree_commons import TreeNode, build_tree


def is_bst(node: Optional[TreeNode], low: float, high: float) -> bool:
    if not node:
        return True

    is_current_node_good = low < node.val < high

    return (
        is_current_node_good
        and is_bst(node.left, low, node.val)
        and is_bst(node.right, node.val, high)
    )


arr = [10, 5, 15, None, None, 6, 20]
tree = build_tree(arr, 0)
if tree:
    print("Is Binary Search Tree:", is_bst(tree, float("-inf"), float("inf")))


"""
## 🧩 **Validate Binary Search Tree (BST)**

---

## 📌 Problem

Check if a binary tree is a **valid BST**

---

## 🧠 What is a valid BST?

For every node:

```text
Left subtree → all values < node.val
Right subtree → all values > node.val
```

---

## 🔍 Example 1

```text
        2
       / \
      1   3
```

👉 Output: `True`

---

## 🔍 Example 2

```text
        5
       / \
      1   4
         / \
        3   6
```

👉 Output: `False`

### Why?

```text
3 is in right subtree of 5 but < 5 ❌
```

---

## 🔍 Example 3

```text
        10
       /  \
      5    15
          /  \
         6    20
```

👉 Output: `False`

---

## ⚠️ Important trap

```text
Checking only immediate children is NOT enough
```

---

## 🧪 Edge Case

```text
[2,2,2] → False
```

👉 duplicates NOT allowed

---

Take your time.

This one is **very important** — it will test whether you truly understood:

* “propagating constraints down the tree” (same concept as your v2)

---

Send your attempt when ready.

"""
