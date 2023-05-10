class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -1

        # brute fore approach of checking every pair of walls
        for i in range(len(height)):
            # note that there can be a slight optimization by doing j in range(i + 1, len(height)) but it doesn't help any of the testcases
            for j in range(len(height)):
                # abs to get the horizontal distance (length / base) of the container
                # min to get the lower of the two vertical distances (breadth / height) of the container. lower because the container can only hold water to that point
                # and simply updating max_area to higher value if found
                max_area = max(max_area, abs(i - j) * min(height[i], height[j]))

        return max_area