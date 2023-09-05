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

    # standard recursive inorder traversal of left, root, right
    def inorder(self, root, populate):
        if not root:
            populate.append(None)
            return
        self.inorder(root.left, populate)
        populate.append(root.val)
        self.inorder(root.right, populate)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # reset values for leetcode "caching"
        self.left_inorder = []
        self.right_inorder = []

        # populate left and right lists
        self.inorder(root.left, self.left_inorder)
        self.inorder(root.right, self.right_inorder)

        # check if the left list is 1:1 same as the reversed (mirrored) right list. again, it fails edge cases where the tree isn't symmetric but the leaf values are same as in above example
        return self.left_inorder == self.right_inorder[::-1]

        # I was explaining this issue to Ara and was rubber ducky-ing the approach of passing in some additional information besides just the values of the nodes for comparison and she suggested recording whether a Node is a "left" or "right" child along with the value which indeed works! just isn't a very elegant solution
        # It's in Leetcode/101. Symmetric Tree (initial inelegant solution).py