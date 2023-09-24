# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # this is a kinda unintuitive iterative solution I just learned out of FOMO (from geeksforgeeks.org/inorder-tree-traversal-without-recursion). this sequence seems counterintuitive because I am used to left-root-right for inorder recursively

        stack = []
        inorder = []
        current = root
        
        while True:

            # if we're looking at non-empty node
            if current:

                # push to stack (and keep going left)
                stack.append(current)

                # this way, the last element to be popped out of the stack (at the else block will be the left-most element; which is what we want in inorder)
                current = current.left
            
            # if we're looking at empty node, it means we've reached the left-most
            elif stack:

                # pop (left-most), at a time
                current = stack.pop()

                # appending popped element to inorder list (which abides to the left-*root*-right pattern)
                inorder.append(current.val)

                # after left and root are done, go right
                current = current.right
            
            # if current is none and also stack is empty, it means we have reached right-most
            else:
                break
        
        return inorder