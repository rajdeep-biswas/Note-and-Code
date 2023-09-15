# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    path_sums = []

    def findPathSums(self, node, path_sum):
        if not node:
            return
        
        if not node.left and not node.right:
            self.path_sums.append(path_sum + node.val)

        self.findPathSums(node.left, path_sum + node.val)
        self.findPathSums(node.right, path_sum + node.val)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        self.path_sums = []
        self.findPathSums(root, 0)
        print(self.path_sums)

        return targetSum in self.path_sums