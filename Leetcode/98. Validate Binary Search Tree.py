# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # going with a no-brainer solution of traversing the tree in-order, populating a list
    # and then checking if the list is sorted

    inOrderTrav = []

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            self.inOrderTrav.append(root.val)
            self.inOrder(root.right)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.inOrderTrav = []

        self.inOrder(root)

        for i in range(len(self.inOrderTrav) - 1):
            if self.inOrderTrav[i] >= self.inOrderTrav[i + 1]:
                return False
        
        return True