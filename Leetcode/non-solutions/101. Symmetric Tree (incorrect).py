# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    """
    This is not a timeout error case, it's just plain wrong; 195/198 testcases.

    Fails the edge case -
        1
       / \
      2   2
     /   /
    2   2

    Because both the left and right child in-order traversals result into [None, 2, None, 2, None]. Had the bottom elements been anything besides '2', it would succeed.
    It's not even advisable to compare the results of traversals of two trees because they're not indicative of whether or not two trees are symmetric, same, etc.
    """
    left_inorder = []
    right_inorder = []

    def inorder(self, root, populate):
        if not root:
            populate.append(None)
            return
        self.inorder(root.left, populate)
        populate.append(root.val)
        self.inorder(root.right, populate)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.left_inorder = []
        self.right_inorder = []
        
        self.inorder(root.left, self.left_inorder)
        self.inorder(root.right, self.right_inorder)
        
        print(self.left_inorder, self.right_inorder)
        return self.left_inorder == self.right_inorder[::-1]