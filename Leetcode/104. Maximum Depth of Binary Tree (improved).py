# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # another recursive BFS solution
    # Neetcode shows multiple other solutions like iterative BFS and iterative DFS (youtube.com/watch?v=hTM3phVI6YQ), might be worth checking out sometime soon
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # idea is intuitive to me only once I have seen, dry ran and understood the solution once. debug log is there in previous commit of this file
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))