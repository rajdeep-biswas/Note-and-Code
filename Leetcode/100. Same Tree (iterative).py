# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # this is the iterative equiavalent of the recursive DFS solution that I have already solved. to me, this is slightly more intuitive / easier to remember
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # stack because DFS, initialize with two of the nodes
        stack = [(p, q)]

        while stack:

            # pop one pair from stack
            p, q = stack.pop()

            # if both are null, trees are same
            if not p and not q:
                continue # note that we continue looking instead of returning True unlike the recursive solution, and this one needs a return True at the end*

            # if only one of two is null, tree is not symmetric
            if not p or not q:
                return False

            # if values are different, tree are not same
            if p.val != q.val:
                return False

            # push equivalent elements elements to stack
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))

        return True # *the return True at the end, since this is an iterative solution