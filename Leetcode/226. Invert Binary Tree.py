# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    the order of the three operations do not make any difference.
    the recursion calls should be next to each other (again, order does not matter, you can recurse left first or right first).
    the swapping operation can appear either before or after them, just not in between.
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        # it might appear that there is a runtime error here, what if root left and / or right do not exist?
        # answer: python has no issues swapping two variables containing 'None's
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

        """
        PS: I actually sat and dry ran why putting the swap operation in the middle does not work; it's to do with some nodes never getting touched and some leaf nodes being swapped twice. in the example of [4,2,7,1,3,6,9] from leetcode, the two children of the root only get swapped finally, and (1, 3) get swapped twice and 6, 7, 9 never get touched.
        You can putting four print statements {"nothing found, going up", "going left", "going right", and "swapping left, right"} through the code, attempt to dry run what is going to be printed and then check against actual console log
        """