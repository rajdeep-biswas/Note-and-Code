class Solution:

    # following the intuition that my goldman sachs interviewer hinted me with
    # swear to god, do not attempt the dictionary based caching in an actual interview, it's a mindfuck to debug. much better off using lists

    def trap(self, height: List[int]) -> int:
        
        # dictionary that has keys: index, values: tuple(max_left, max_right)
        tracker = dict()

        # populate initial values

        tracker[0] = {"max_left": 0}

        # forward pass to populate max_left of each index
        for i in range(1, len(height)):
            tracker[i] = {"max_left": max(tracker[i - 1]['max_left'], height[i - 1])}
        
        tracker[len(height) - 1]["max_right"] = 0

        # backward pass to populate max_right of each index
        for i in range(len(height) - 2, -1, -1):
            tracker[i]["max_right"] = max(tracker[i + 1]['max_right'], height[i + 1])

        # single pass to populate current height of each index
        for i in range(len(height)):
            tracker[i]['cur'] = height[i]

        accumulated = 0

        # for each index count towards accumulated water
        for i in range(1, len(height) - 1):
            # the outer max is required so that the result of summation doesn't go below zero. (it can happen when current hill is taller than it's possible neighbors)
            accumulated += max(0, min(tracker[i]['max_right'], tracker[i]['max_left']) - tracker[i]['cur'])
        
        return accumulated