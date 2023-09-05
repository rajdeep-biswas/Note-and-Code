# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # with a little help from ChatGPT, this is the iterative equiavalent of the recursive DFS solution that I have already solved. to me, this is slightly more intuitive / easier to remember
    def dfs_iterative(self, left_node, right_node):

        # stack because DFS, initialize with two of the nodes
        stack = [(left_node, right_node)]

        while stack:

            # pop one pair from stack
            left_node, right_node = stack.pop()

            # if both are null, tree is symmetric
            if not left_node and not right_node:
                continue # note that we continue looking instead of returning True unlike the recursive solution, and this one needs a return True at the end*
            
            # if only one of two is null, tree is not symmetric
            if not left_node or not right_node:
                return False

            # if values are different, tree is not symmetric
            if left_node.val != right_node.val:
                return False
            
            # push mirror elements to stack
            stack.append((left_node.left, right_node.right))
            stack.append((left_node.right, right_node.left))
        
        return True # *the return True at the end, since this is an iterative solution

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.dfs_iterative(root.left, root.right)