class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -1
        l = 0
        r = len(height) - 1

        while l < r:
            max_area = max(max_area, (r - l) * min(height[l], height[r]))

            # whichever pointer is of lower height, push that inwards, that way you maximizing your next lookup
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_area

"""
Footnote: if the ifelse block at line 11 feels like there can be edgecases that break it, think of the following things -
1. Know that the lower of two has already found it's maximum area because vertically it itself is the bottleneck, and horizontally, you have already maxed it out by taking the right most index. So it can't get any bigger than that. It's 100% the case an area >= this one can only be found by keeping the taller index.
2. In case when two indices are the same height, you may think it may lead to inconsistent finds depending upon whether you move the right one or the left one. While that *is* true, the intermediate areas that you find can differ depending upon whether you use > or >= at the if condition, but, ultimately the max area will always be found because after the equal indices, the right/left pointers are gonna resume being moved only at the smaller end.
"""