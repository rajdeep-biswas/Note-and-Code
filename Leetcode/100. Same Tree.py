# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    This solution is, in spirit and approach, the exact same as Leetcode/101. Symmetric Tree (elegant).py
    """

    # special implementation of DFS where it doesn't take in one root node, but two root nodes (left and right children of the same root) at the same time, so we can recurse comparatively
    def dfs(self, root_one, root_two):

        # base case 1: if both corresponding Nodes are None, that *is* same tree
        if not root_one and not root_two:
            return True

        # base case 2: if only one of the corresponding Nodes is None, that is not same tree
        if not root_one or not root_two:
            return False

        # (this is the only line that makes the solution different from 101. Symmetric Tree)
        # compare current left and right vals, AND corresponding children; left's left vs right's left AND left's right vs right's right. *dry run this for sure if it doesn't make sense just by reading*
        return root_one.val == root_two.val and self.dfs(root_one.left, root_two.left) and self.dfs(root_one.right, root_two.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)