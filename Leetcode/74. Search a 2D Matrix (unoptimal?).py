class Solution:

    # pretty sure this is a suboptimal solution which I took the inspiration from neetcode but he does it much better
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_top = 0
        row_bot = len(matrix)
        found_row = -1

        # figure out which row our number is in, if it's in the 2D array
        while row_top < row_bot:
            row_mid = (row_top + row_bot) // 2

            if target < matrix[row_mid][0]:
                row_bot = row_mid
            elif target > matrix[row_mid][len(matrix[row_mid]) - 1]:
                row_top = row_mid
            else:
                found_row = row_mid
                break
        
        if found_row == -1:
            return False

        nums = matrix[found_row]
        right = len(nums) - 1
        left = 0

        # figure out which column (index) of said row our target number is in
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return False