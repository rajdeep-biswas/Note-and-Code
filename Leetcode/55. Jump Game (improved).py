class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # watched Neetcode's visual explanation last night and it made sense to me. Coded it up this morning and happy to announce it's 1:1 same as Neetcode's solution
        # actually better than the one that he showed in the video but the improved code he posted later on on his website has caught up to my readability standards ;)
        
        # our goal is to reach the end index
        goalpost = len(nums) - 1

        # run loop backwards from the 2nd last index since we already have the goalpost at the last one
        for i in range(len(nums) - 2, -1, -1):

            # if we get to an index that has a jump value that can surpass the goalpost, our new goal, simply, is just to check if we can get to that index, so we move the goalpost to that index
            if nums[i] + i >= goalpost:
                goalpost = i
        
        # at last we just need to check if our goalpost has made it all the way to the beginning
        return goalpost == 0

        # PS: if this doesn't make sense, I highly recommend watching the visual explanation. it made sense to me right away youtube.com/watch?v=Yan0cv2cLy8