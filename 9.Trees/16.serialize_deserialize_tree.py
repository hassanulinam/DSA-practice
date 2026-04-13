from typing import Optional

from tree_commons import TreeNode, build_tree


def serialize_tree_preorder(root: TreeNode) -> str:
    elements = []

    def dfs(node: Optional[TreeNode]):
        if not node:
            elements.append(None)
            return
        elements.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(map(lambda x: "null" if x is None else str(x), elements))


def deserialize_tree_preorder2(s: str) -> Optional[TreeNode]:
    lst = s.split(",")
    i = 0

    def dfs() -> Optional[TreeNode]:
        nonlocal i
        if lst[i] == "null":
            i += 1
            return None

        curr = TreeNode(int(lst[i]))
        i += 1
        curr.left = dfs()
        curr.right = dfs()
        return curr

    return dfs()


arr = [1, 2, 3, None, None, 4]
root = build_tree(arr, 0)
if root:
    inorder_serial = serialize_tree_preorder(root)
    print("PreOrder Serailization", inorder_serial)
    deserialized_tree = deserialize_tree_preorder2(inorder_serial)
    if deserialized_tree:
        print("Deserialized string:", serialize_tree_preorder(deserialized_tree))
    else:
        print("No tree formed in deserialization")
