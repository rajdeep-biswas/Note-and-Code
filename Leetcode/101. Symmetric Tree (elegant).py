# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # this is a special implementation of DFS where it doesn't take in one root node, but two root nodes (left and right children of the same root) at the same time, so we can recurse comparatively
    def dfs(self, left, right):

        # base case 1: if both mirror'd Nodes are None, that *is* symmetric
        if not left and not right:
            return True
        
        # base case 2: if only one of the mirror'd Nodes is None, that is not symmetric
        if not left or not right:
            return False
        
        # compare current left and right vals, AND mirror'd children; left's left vs right's right AND right's left vs left's right. *dry run this for sure if it doesn't make sense just by reading*
        return left.val == right.val and self.dfs(left.left, right.right) and self.dfs(right.left, left.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # single and simple call to recursive method
        return self.dfs(root.left, root.right)