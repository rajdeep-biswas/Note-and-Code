# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # this is a special implementation of DFS where it doesn't take in one root node, but two root nodes (left and right children of the same root) at the same time, so we can recurse comparatively
    def dfs(self, left_node, right_node):

        # base case 1: if both mirror'd Nodes are None, that *is* symmetric
        if not left_node and not right_node:
            return True
        
        # base case 2: if only one of the mirror'd Nodes is None, that is not symmetric
        if not left_node or not right_node:
            return False
        
        # compare current left and right vals, AND mirror'd children; left's left vs right's right AND right's left vs left's right. *dry run this for sure if it doesn't make sense just by reading*
        return left_node.val == right_node.val and self.dfs(left_node.left, right_node.right) and self.dfs(left_node.right, right_node.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # single and simple call to recursive method
        return self.dfs(root.left, root.right)