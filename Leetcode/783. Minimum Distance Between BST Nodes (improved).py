# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # slightly modified version of Neetcode's

    minm = None
    prev = None

    # standard recursive in-order traversal method with a slight twist
    def inOrder(self, node):

        if not node:
            return

        self.inOrder(node.left)

        # instead of storing to list / printing in-order, we do the operation that we want to in-order. how we tweak recursive functions is starting to make sense to me!
        if self.prev:
            self.minm = min(self.minm, node.val - self.prev.val)
        self.prev = node

        self.inOrder(node.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        self.minm = float("inf") # library feature you didn't know existed!
        self.prev = None

        self.inOrder(root)

        return self.minm