"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    dfs_trav = None
    visited = None

    def __init__(self):
        self.dfs_trav = []
        self.visited = set()

    # I wrote this DFS solution on my own, even though it's not useful towards solving the problem. Just wanted to save this and nothing else.
    def dfs(self, node):
        q = []
        q.insert(0, node)
        self.visited.add(node)

        while q:
            cur = q.pop()
            if cur:
                self.dfs_trav.append(cur.val)

                for neighbor in cur.neighbors:
                    if neighbor not in self.visited:
                        q.insert(0, neighbor)
                        self.visited.add(neighbor)

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        print("main node.val:", node.val)
        self.dfs(node)
        print(self.dfs_trav)
