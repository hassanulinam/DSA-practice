# https://leetcode.com/problems/populating-next-right-pointers-in-each-node
from collections import deque
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional["Node"]) -> Optional["Node"]:
        if not root:
            return root
        q = deque([root])
        while q:
            size = len(q)
            prev: Node | None = None
            for _ in range(size):
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
