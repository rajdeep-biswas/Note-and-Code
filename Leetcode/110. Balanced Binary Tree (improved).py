# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # same solution as neetcode's. i just made it a bit more readable (and a bit more verbose) by using named dictionary keys instead of list indices

    def dfs(self, node):

        # we use two different information; if the left and right subtrees so far are indeed balanced and to check that we will also need to depth (height) found so far
        if not node:
            return {"balanced": True, "depth": 0} # if empty node, it is by default balanced and contributes to a depth of 0 (base case)
        
        # recurse left and right
        left_tree = self.dfs(node.left)
        right_tree = self.dfs(node.right)

        # using a boolean variable where a node is balanced if both its children themselves are balanced and also the absolute difference of their depths in not more than 1
        balanced = left_tree['balanced'] and right_tree['balanced'] and abs(left_tree['depth'] - right_tree['depth']) <= 1

        # returning the boolean and the depth found so far (the depth key is the entire program that is #104)
        return {"balanced": balanced, "depth": max(left_tree['depth'], right_tree['depth']) + 1}


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.dfs(root)['balanced']