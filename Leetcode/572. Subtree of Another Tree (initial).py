# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # my initial brute force solution O(n^2) (it simplifies from O(n + m + n ^ 2)) where n is the main tree and m is the sub-tree
    mainTrav = []
    subTrav = []
    rootfinds = []

    # dfs-esque search that finds all nodes on the main tree that have the same root value as the subtree
    def findRoot(self, node, subRootVal):
        if not node:
            return None

        # there might be multiple nodes that carry that value, so we need to look for matching trees on all of them (also why it needs to be a list)
        if node.val == subRootVal:
            self.rootfinds.append(node)

        self.findRoot(node.left, subRootVal)
        self.findRoot(node.right, subRootVal)

    # standard in-order traversal that populates a list based on passed in parameter for comparison (same tree will give us same in order array)
    def inorder(self, node, arr):

        if not node:
            return None

        self.inorder(node.left, arr)

        arr.append(node.val)

        self.inorder(node.right, arr)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.rootfinds = []
        self.subTrav = []

        self.findRoot(root, subRoot.val)

        # this only needs to be found once
        self.inorder(subRoot, self.subTrav)

        if not self.rootfinds:
            return False

        # beginning from each root of the main tree, check for match with subtree
        for rootfind in self.rootfinds:
            self.mainTrav = []

            # in-order traverse a main tree but only from each "matching root" we have found with the subtree
            self.inorder(rootfind, self.mainTrav)

            # we only needed to get subTrav once since that won't be changing
            if self.mainTrav == self.subTrav:
                return True

        return False