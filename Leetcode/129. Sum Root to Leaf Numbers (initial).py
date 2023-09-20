# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # my one-shot solution based on intuition from problems like #543 (maybe? I dont even know which exact problem(s) helped in the exact intuition for this kind of recursion)
    # I will look at neetcode's solution and see if it's an improvement

    numbers = []

    # intuitive DFS recursion. pass down a number starting from 0, and "append" digits to lsb
    def getNumbers(self, node, num):
        if not node:
            return 0

        # num is initially zero
        num = num * 10 + node.val

        # the condition is a check for leaf node. it's only a leaf node if both its children are missing
        if not node.left and not node.right:
            # storing to member list
            self.numbers.append(num)

        # recurse left and right while passing down the updated number root-to-leaf
        self.getNumbers(node.left, num)
        self.getNumbers(node.right, num)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.numbers = []
        self.getNumbers(root, 0)

        # answer is a simple sum of all numbers found so far. keeps it at O(n) time and space
        return sum(self.numbers)