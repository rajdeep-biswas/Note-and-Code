# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # I found this solution submitted on March 13th (~190 days ago) 

    height = 0
    levelOrderTrav = []

    def getHeight(self, root, height):
        if root:
            if height > self.height:
                self.height = height
            if root.left:
                self.getHeight(root.left, height + 1)
            if root.right:
                self.getHeight(root.right, height + 1)


    def findAtHeight(self, root, curHeight, searchHeight):
        if curHeight == searchHeight - 1:
            foundList = []
            if root.left:
                foundList.append(root.left.val)
            if root.right:
                foundList.append(root.right.val)
            print(curHeight, searchHeight, foundList)
            if foundList:
                print("returning found list", foundList)
                return foundList

        if root:
            curHeight += 1
            if root.left:
                self.findAtHeight(root.left, curHeight, searchHeight)
            if root.right:
                self.findAtHeight(root.right, curHeight, searchHeight)


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levelOrderTrav = []

        self.getHeight(root, 0)
        height = self.height

        if root:
            self.levelOrderTrav.append([root.val])

        for i in range(height):
            print("loop i", i)
            foundList = self.findAtHeight(root, 0, i + 1)
            print("received found list", foundList)
            if foundList:
                print("appending list", foundList)
                self.levelOrderTrav.append(foundList)

        print("levelOrderTrav", self.levelOrderTrav)
        return self.levelOrderTrav