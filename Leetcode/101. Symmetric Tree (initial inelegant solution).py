# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    """
    I was Rubber ducky-ing Ara the issue with `Leetcode/non-solutions/101. Symmetric Tree (incorrect).py` and this is the result.
    """

    left_inorder = []
    right_inorder = []

    # standard recursive inorder traversal of left, root, right with an addition of recording the "direction" of the node (left, right or root)
    def inorder(self, root, populate, direction):
        if not root:
            populate.append((None, direction))
            return
        self.inorder(root.left, populate, "left")
        populate.append((root.val, direction))
        self.inorder(root.right, populate, "right")

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # reset values for leetcode "caching"
        self.left_inorder = []
        self.right_inorder = []

        # populate left and right lists
        self.inorder(root.left, self.left_inorder, "root")
        self.inorder(root.right, self.right_inorder, "root")
        # reverse right list
        self.right_inorder = self.right_inorder[::-1]

        i = 0 # check length of both trees in case of unbalanced trees
        while i < len(self.left_inorder) and i < len(self.right_inorder):

            # check if you are looking at the root nodes (at index[1])
            if self.left_inorder[i][1] == 'root' and self.right_inorder[i][1] == 'root':

                # check if the values don't match, that's an instant mismatch of symmetry (at index[0])
                if self.left_inorder[i][0] != self.right_inorder[i][0]:
                    return False

                # if values do match, we skip rest of the iteration
                i += 1
                continue

            # maintain two flag variables (the fact they are True and False is already inelegant)
            elements_match = True
            directions_symmetric = False

            # simple check on elemnts index[0] matching
            if self.left_inorder[i][0] != self.right_inorder[i][0]:
                elements_match = False

            # explicit check on whether the directions of compared elements are exact opposite (since 'right' == 'root', for example, is also 'False' but with so many moving parts of other conditions, it breaks on some edge cases if simplified any further)
            if self.left_inorder[i][1] == 'right' and self.right_inorder[i][1] == 'left' or self.left_inorder[i][1] == 'left' and self.right_inorder[i][1] == 'right':
                directions_symmetric = True

            # if either the elements don't match or directions are not symmetric, we return False
            if not (elements_match and directions_symmetric):
                return False

            # increment to look at next pair
            i += 1

        # if nothing has been proven wrong within the loop, the tree is indeed symmetric
        return True