# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # I got a pretty close intuitive solution. Just had to remove one bug after getting confidence by looking at Neetcode's solution and knowing he did the exact 1:1 solution as mine

    st = ''

    # tweaked preorder is indeed appropriate for this (as question suggests)
    def preorder(self, node):
        
        if not node:
            return

        # initiate first opening parenthesis and element
        self.st += '('
        self.st += str(node.val)

        # if current node's left child doesnt exist but right child does we need an '()' to represent the absence, according to the spec.
        # note that this method works both if placed before the left recursion call or after it. but not after the right recursion call. dry run to understand why
        if not node.left and node.right:
            self.st += '()'

        # recurse left
        self.preorder(node.left)

        # recurse right
        self.preorder(node.right)

        # put closing parenthesis after right recursion
        self.st += ')'

    def tree2str(self, root: Optional[TreeNode]) -> str:

        self.st = ''

        self.preorder(root)

        # get rid of outermost opening and closing parentheses
        return self.st[1:-1]