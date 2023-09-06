"""
Exact same problem and solution as #783.
Check out Leetcode/783. Minimum Distance Between BST Nodes (improved).py for comments
"""

class Solution:

    prev = None
    minm = None

    def inOrder(self, node):
        if not node:
            return
        
        self.inOrder(node.left)
        
        if self.prev:
            self.minm = min(self.minm, node.val - self.prev.val)
        self.prev = node

        self.inOrder(node.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.prev = None
        self.minm = float("inf")

        self.inOrder(root)

        return self.minm