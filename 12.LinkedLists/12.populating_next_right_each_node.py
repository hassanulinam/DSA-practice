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
        vertical = root
        while vertical.left:
            horizontal = vertical
            while horizontal:
                horizontal.left.next = horizontal.right
                if horizontal.next:
                    horizontal.right.next = horizontal.next.left
                horizontal = horizontal.next

            vertical = vertical.left
        return root
