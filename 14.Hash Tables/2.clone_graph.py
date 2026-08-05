# https://leetcode.com/problems/clone-graph

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node
        seen = {}

        def dfs(node: Node):
            if node.val in seen:
                return seen[node.val]
            current = Node(node.val)
            seen[node.val] = current
            for nb in node.neighbors:
                current.neighbors.append(dfs(nb))
            return current

        return dfs(node)
