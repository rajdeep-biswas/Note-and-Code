class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # O(log n + log m) time where n is number of rows and m is number of columns

        # identifying row using standard binary search, first
        top, bot = 0, len(matrix) - 1
        ncol = len(matrix[0])

        # row_i is meant to keep track of having found a suitable row
        row_i = -1

        while top <= bot:

            m = (top + bot) // 2

            # we look if the target element is sized between the first and last elements of the middle row that we're looking at
            if target >= matrix[m][0] and target <= matrix[m][ncol - 1]:
                row_i = m
                break
            
            # if not we go to higher or lower row depending upon whether the target is larger than the last element of the middle row
            elif target > matrix[m][ncol - 1]:
                top = m + 1
            
            # or if it's smaller than the first element of the middle row.
            # redundant check would be elif target < matrix[m][0]
            else:
                bot = m - 1

        # break out for efficiency if target is out of bounds of the matrix elements
        if row_i == -1:
            return False

        # identifying column, using standard binary search
        l, r = 0, ncol - 1

        while l <= r:

            m = (l + r) // 2

            if target == matrix[row_i][m]:
                return True
            
            elif target > matrix[row_i][m]:
                l = m + 1
            
            else:
                r = m - 1
        
        return False