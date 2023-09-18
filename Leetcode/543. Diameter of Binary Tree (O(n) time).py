# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # found this solution in the comment section of Neetcode's explanation youtube video (youtube.com/watch?v=bkxqA8Rfv04). this is a more elegant and readable version of neetcode's and i like it
    # for the most part, it's an O(N) improvement over my brute force solution Leetcode/543. Diameter of Binary Tree (initial).py which was O(n^2)

    diameter = 0

    # this is more like a post-order traversal that looks and left and right subtree depths and then updates diameter variable. the return statement is also needed to populate the left and right variables
    def dfs(self, node):

        if not node:
            return 0

        left_diam = self.dfs(node.left)
        right_diam = self.dfs(node.right)

        self.diameter = max(self.diameter, left_diam + right_diam)

        # the purpose of this is to populate the variables so that we can update the diameter variable
        # it may appear that this should work by itself (since in some cases both the final value of diameter and the final return value may be the same) but actually, this in itself will finally just return the max depth of the tree (remember 104?) we are just using this functionality to keep track of the max diameter encountered so far. (I mean this does seem a bit hacky but it is indeed O(n))
        return 1 + max(left_diam, right_diam)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0

        self.dfs(root)

        return self.diameter