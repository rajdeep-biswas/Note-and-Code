# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Nick White's explanation made sense to me (youtube.com/watch?v=12omz-VAyRk) though he's using Java. Code logically the same as Neetcode's but his drawing explanation was a total mindfuck, so I had to look elsewhere
    root = None

    # basically the same logic as standard binary search, just that instead of if conditions doing divide and conquer, we populate all elements
    def makeTree(self, nums, left, right):
        if right < left:
            return None
        
        mid = (right + left) // 2
        node = TreeNode(nums[mid])

        node.left = self.makeTree(nums, left, mid - 1)
        node.right = self.makeTree(nums, mid + 1, right)

        return node
        

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        self.root = None
        return self.makeTree(nums, 0, len(nums) - 1)