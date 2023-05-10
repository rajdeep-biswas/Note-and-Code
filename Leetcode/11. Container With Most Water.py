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