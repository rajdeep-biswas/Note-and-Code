# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # solution I thought up that DFS's into one root-to-leaf path at a time and stores the summed value into set, via recursion
    path_sums = set()

    def findPathSums(self, node, path_sum):

        # standard base case. note: i had written the .add() here but that not only creates duplicates of every root-to-leaf sum but also creates incorrect entries where either left or right child are missing. this is handled better at line 18
        if not node:
            return

        # we consider a leaf node only when it doesn't have any further left or right children, so this is the safest way to record sums
        if not node.left and not node.right:
            self.path_sums.add(path_sum + node.val)

        # recurse left and right. *no need to return anything since our if condition is adding into a member variable, that's all the information we need
        self.findPathSums(node.left, path_sum + node.val)
        self.findPathSums(node.right, path_sum + node.val)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        self.path_sums = set()
        self.findPathSums(root, 0)
        print(self.path_sums)

        return targetSum in self.path_sums