# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # slightly better solution that I thought up that uses a counter. and is O(1) space

    count = 0
    kthsmallest = None

    def inOrder(self, node, k):

        if not node:
            return None

        self.inOrder(node.left, k)

        # counter starts counting only once it reaches the left-most node (smallest)
        self.count += 1

        # once the counter value reaches k it means we have reached the k-th smallest value in-order.
        # note that k being 1-indexed works out just fine because we're incrementing it *before* the condition
        if self.count == k:

            # this setting member variable is the least favorite part of mine of the code. it's pretty inelegant, I am gonna watch neetcode after this
            self.kthsmallest = node.val

            # this return doesn't even improve performance besides skipping the right subtree of only the element we're looking for
            return
        
        self.inOrder(node.right, k)
        

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = 0
        self.kthsmallest = None
        
        self.inOrder(root, k)

        return self.kthsmallest