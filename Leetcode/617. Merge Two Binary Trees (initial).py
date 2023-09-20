# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # O(n) solution where I use dual-root DFS methods. I need two methods because doing it in the same method results in incorrectly summing nodes to itself *after* merging them (which should be just merged and not summed again)
 
    # recursively adds values as long as correspnding nodes exist, pretty intuitive
    def addValues(self, node1, node2):

        # base case that checks both nodes exist (are not None)
        if not node1 and not node2:
            return None
        
        # we use the first tree (node1) for the result (this is mentioned in the main method too)
        if node1 and node2:
            node1.val += node2.val
        
        # recurse left and right as long as both exist
        if node1 and node2:
            self.addValues(node1.left, node2.left)
            self.addValues(node1.right, node2.right)
    

    # recursively merges ("combines") None nodes in tree1 where corresponding nodes do exist in tree2
    def combineNodes(self, node1, node2):

        # base case that checks both nodes exist (are not None)
        if not node1 and not node2:
            return None
        
        # check if both root node and their corresponding left nodes exist, otherwise it throws error. (a bit inelegant but works)
        if node1 and not node1.left and node2 and node2.left:
            node1.left = node2.left
        
        # equivalent condition as above but for right nodes
        if node1 and not node1.right and node2 and node2.right:
            node1.right = node2.right
        
        # recurse left and right as long as both exist
        if node1 and node2:
            self.combineNodes(node1.left, node2.left)
            self.combineNodes(node1.right, node2.right)


    # main method where we consider root1 the main tree and merge root2 into it. do not need any additional space that way
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        # handle corner case where root1 is None but root2 is not (if root2 is None, root1 anyway gets returned at the end)
        if not root1 and root2:
            return root2

        # we add values *before* combining nodes because combining first would be incorrect because it'll be summing missing nodes with itself
        self.addValues(root1, root2)
        self.combineNodes(root1, root2)
        
        return root1