class Solution:

    paths = []
    cur_path = []

    # came up with my own solution to use two different lists
    # the tricky part was at what point in the code should you pop from the cur_path list
    def dfs(self, root):

        # standard dfs base case
        if not root:
            return

        # if element is in path, added it. nothing too clever
        self.cur_path.append(str(root.val))

        # if neither left or right exist, must mean we've arrived at a leaf node. so we append the found path to the main list
        if not root.left and not root.right:
            self.paths.append(self.cur_path.copy()) # you need a .copy() to pass in a deepcopy

        # standard left and right recursion
        if root.left:
            self.dfs(root.left)
        
        if root.right:
            self.dfs(root.right)
        
        # just one of these at the bottom does the trick because we're only popping elements one at a time as we're making our way back up the tree. doing a dry run is the best way to visualize this
        self.cur_path.pop()


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        self.paths = []
        self.cur_path = []

        self.dfs(root)

        # I was too lazy to do formatting while appending
        sanitized = []
        for path in self.paths:
            sanitized.append('->'.join(path))

        return sanitized