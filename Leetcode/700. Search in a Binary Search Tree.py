# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # simple binary search logic, just in a tree format
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # base case
        if not root:
            return None

        if root.val > val:

            # IMPORTANT: in my first run, I was missing the concept that I am supposed to not just call the method recursively but also return the value from all the way down in the call stack
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return root