# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depths = []

    # standard maxDepth method from #104
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

    # standard in-order traversal that looks at every node
    def traverseAll(self, node):
        if not node:
            return
        
        self.traverseAll(node.left)

        # my idea here was to take the sum of longest left depth and longest right depth (since we are doing this for every node, we will store all possible path lengths)
        self.depths.append(sum([self.maxDepth(node.left), self.maxDepth(node.right)]))

        self.traverseAll(node.right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 1
        
        self.depths = []

        self.traverseAll(root)

        # the highest of all the path lengths is the "diameter" of the tree
        return max(self.depths)