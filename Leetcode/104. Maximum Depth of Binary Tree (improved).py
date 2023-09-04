# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # this is a debug console log commit that I use to verify my dry runs, will overwrite with a proper commit
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            print("nothing found returning 0")
            return 0
        print("going left", root.left.val if root.left else None)
        max_left = self.maxDepth(root.left)
        print("going right", root.right.val if root.right else None)
        max_right = self.maxDepth(root.right)
        print("returning 1 +", max(max_left, max_right), "from", root.val)
        return 1 + max(max_left, max_right)