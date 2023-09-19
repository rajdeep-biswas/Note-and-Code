# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # the whole solution that is Leetcode/100. Same Tree.py
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # standard base case
        if not root:
            return False

        # check if current node of main tree matches the subtree
        if self.isSameTree(root, subRoot):
            return True

        # if not recursively check left and right
        # we don't need any additonal return False at the end because if no subtree was found to be matching (down at the depths of recursion), this is gonna return False or False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)