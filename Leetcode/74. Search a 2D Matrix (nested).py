class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # O(log n + log m) time where n is number of rows and m is number of columns
        # nested solution of Leetcode/74. Search a 2D Matrix (initial).py, just because I can. that one is way more readable.

        # identifying row using standard binary search, first
        top, bot = 0, len(matrix) - 1
        ncol = len(matrix[0])

        # row_i is meant to keep track of having found a suitable row
        row_i = -1

        while top <= bot:

            m_row = (top + bot) // 2

            # we look if the target element is sized between the first and last elements of the middle row that we're looking at
            if target >= matrix[m_row][0] and target <= matrix[m_row][ncol - 1]:

                # identifying column, using standard binary search
                l, r = 0, ncol - 1

                while l <= r:

                    m_col = (l + r) // 2

                    if target == matrix[m_row][m_col]:
                        return True
                    
                    elif target > matrix[m_row][m_col]:
                        l = m_col + 1
                    
                    else:
                        r = m_col - 1
                
                # while removing this return will still keep the code at O(log n + log m) but it does speed up the solution a bit by skipping redundant outer iterations
                return False
            
            # if not we go to higher or lower row depending upon whether the target is larger than the last element of the middle row
            elif target > matrix[m_row][ncol - 1]:
                top = m_row + 1
            
            # or if it's smaller than the first element of the middle row.
            # redundant check would be elif target < matrix[m][0]
            else:
                bot = m_row - 1

        return False