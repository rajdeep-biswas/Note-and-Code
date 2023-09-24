# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # I was expecting this solution to be a reorder of operations of #94 but turns out it's an entire different solution

        preorder = []
        stack = []

        stack.append(root)

        while stack:

            current = stack.pop()
            if current:
                preorder.append(current.val)

                # made sense 'til this part. now suddenly we have right before left (for preorder root-left-right), *because* it's a stack.
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
        
        return preorder