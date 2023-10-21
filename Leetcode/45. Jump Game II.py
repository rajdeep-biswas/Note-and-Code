class Solution:
    def jump(self, nums: List[int]) -> int:

        # based on my understanding of neetcode's video explanation youtube.com/watch?v=dJ7sWiOoK7g.

        jumps = 0
        l = r = 0

        while r < len(nums) - 1:

            farthest = 0
            # The inner loop iterates from l to r, which doesn't necessarily mean it's quadratic. The number of iterations in the inner loop depends on the values of l and r, and these values are not directly related to the size of the nums array. In the worst case, the inner loop could potentially iterate over the entire array, but it doesn't do so for every value of r. - ChatGPT
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            jumps += 1
        
        return jumps

        # PS: I have too much on my mind to explain all of this in comments, the visual explanation in the video does a great job