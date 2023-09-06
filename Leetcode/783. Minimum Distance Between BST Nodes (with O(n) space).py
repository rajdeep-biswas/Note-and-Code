# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # In-order traversal is how you get elements out of a BST in sorted-order. (added TIL on readme.md 6th September)
    in_order = []
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.in_order.append(root.val)
        self.inOrder(root.right)

    # pretty intuitive adjacent differencing and returning min
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.in_order = []
        self.inOrder(root)

        diffs = []
        for i in range(len(self.in_order) - 1):
            diffs.append(self.in_order[i + 1] - self.in_order[i])

        return min(diffs)