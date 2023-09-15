# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # another version of my solution where we check if we have reached the target sum as and when we reach each leaf node
    # this is the exact same solution Needcode does, except he doesn't use variables and uses slightly more elegant boolean logic at line 24
    # for other parts to make sense, check comments on Leetcode/112. Path Sum.py

    def findPathSums(self, node, path_sum, targetSum):
        if not node:
            return

        if not node.left and not node.right:
            if path_sum + node.val == targetSum:
                return True

        left_bool = self.findPathSums(node.left, path_sum + node.val, targetSum)
        right_bool = self.findPathSums(node.right, path_sum + node.val, targetSum)

        if left_bool or right_bool:
            return True

        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        return self.findPathSums(root, 0, targetSum)