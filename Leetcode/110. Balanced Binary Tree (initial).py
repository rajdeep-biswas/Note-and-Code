# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    depth_pairs = []

    # reusing this method from 104 (improved)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # standard inorder traversal with a twist on the middle case
    # idea is to traverse every node and store the max depth of each node's left and right subtrees in pairs
    # that is O(n) space for sure. now whether is it O(n^2) time or O(nlogn), I am not quite sure. (the latter is possible since as we are descending down the tree, the inner loop is only looking at children)
    def inOrder(self, node):
        if not node:
            return

        self.inOrder(node.left)

        self.depth_pairs.append((self.maxDepth(node.left), self.maxDepth(node.right)))

        self.inOrder(node.right)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.depth_pairs = []

        self.inOrder(root)

        for depth_pair in self.depth_pairs:

            # if the depth of the left and right subtrees of any node has a difference of greater than 1, then it's not a balanced BT
            if abs(depth_pair[0] - depth_pair[1]) > 1:
                return False
        return True

    # i am too sleepy and forgot what I was originally planning to do lol, so just made this up
    # i had something else in mind in as how i was gonna combine these three methods. but this does work. so i am gonna call it a night