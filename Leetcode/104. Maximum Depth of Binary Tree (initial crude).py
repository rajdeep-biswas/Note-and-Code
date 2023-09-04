class Solution:
    depth = -1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.getHeight(root, 0)
        return self.depth + 1

    # used this from a previous solution I had coded (102. Binary Tree Level Order Traversal)
    def getHeight(self, root, height):
        if root:
            if height > self.depth:
                self.depth = height
            if root.left:
                self.getHeight(root.left, height + 1)
            if root.right:
                self.getHeight(root.right, height + 1)