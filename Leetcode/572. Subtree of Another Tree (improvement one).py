# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    truths = []
    
    # the whole solution that is Leetcode/100. Same Tree.py
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    # look at all main tree elements and populate an array with truth values
    def traverseAll(self, node, subRoot):
        if not node:
            return

        self.traverseAll(node.left, subRoot)

        self.truths.append(self.isSameTree(node, subRoot))

        self.traverseAll(node.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.truths = []

        self.traverseAll(root, subRoot)

        # if any one has matched, we can return true. we can also write a more elegant solution. will be named something along the lines of Leetcode/572. Subtree of Another Tree (improvement two).py
        return True in self.truths