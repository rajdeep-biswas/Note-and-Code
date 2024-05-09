class Solution:

    # following the intuition that my goldman sachs interviewer hinted me with
    # swear to god, do not attempt the dictionary based caching in an actual interview, it's a mindfuck to debug. much better off using lists

    def trap(self, height: List[int]) -> int:
        
        # list for keeping track of highest hill to the left of index i
        max_lefts = [0] * len(height)
        max_rights = [0] * len(height)

        # forward pass to populate max_left of each index
        for i in range(1, len(height)):
            max_lefts[i] = max(max_lefts[i - 1], height[i - 1])
    
        # backward pass to populate max_right of each index
        for i in range(len(height) - 2, -1, -1):
            max_rights[i] = max(max_rights[i + 1], height[i + 1])

        accumulated = 0

        # for each index count towards accumulated water
        for i in range(1, len(height) - 1):
            # the outer max is required so that the result of summation doesn't go below zero. (it can happen when current hill is taller than it's possible neighbors)
            accumulated += max(0, min(max_rights[i], max_lefts[i]) - height[i])
        
        return accumulated