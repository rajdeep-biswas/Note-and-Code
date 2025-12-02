# i actually solved this pas midnight of Nov 21 (i.e. Nov 22). check personal logs if interested in the backstory

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # every even row (index) has extra spaces
        # characters are to be populated columns-first given a number of rows
        # when number of rows are exhausted, we're supposed to move to the next column
        # when at next column, we're supposed to begin at nrow - 2
        # and scroll up until we hit column index 1
        # this keeps rotating
        # i can populate this in a linear (row-first) manner and then "transpose the matrix"

        # row zero gets populated fully
        # so does every row where row_idx % numRows - 1 is 0

        # base case
        if len(s) == 1 or numRows == 1:
            return s

        # construct a 2D array with max possible length and breadth
        global_array = [[f'' for i in range(numRows)] for j in range(len(s))] # {i},{j}

        # go through string index one by one
        str_idx = 0

        # set a rotating column index that will take care of the columns with diagonal population
        rotating_col_idx = numRows - 2

        for row_idx in range(len(global_array)):
            for col_idx in range(len(global_array[row_idx])):

                # if string length exceeded
                if str_idx >= len(s):

                    # deconstruct result string from transposed matrix
                    res_str = ''
                    for col_idx in range(len(global_array[0])):
                        for row_idx in range(len(global_array)):
                            res_str += global_array[row_idx][col_idx]
                            
                    return res_str

                # fill entire row when index is at intervals of numRows - 1
                if not row_idx % (numRows - 1):
                    global_array[row_idx][col_idx] = s[str_idx]

                # for non-interval i.e. diagonal rows, fill characters according to rotating col index
                else:

                    # reset when you've hit zero
                    if rotating_col_idx <= 0:
                        rotating_col_idx = numRows - 2
                    
                    global_array[row_idx][rotating_col_idx] = s[str_idx]
                    str_idx += 1
                    rotating_col_idx -= 1
                    break
                
                str_idx += 1


"""

"PAYPALISHIRING"

numRows = 4

P A Y P | row_idx = 0, row_idx % numRows - 1 = 0
    A   | row_idx = 1, row_idx % numRows - 1 = 1
  L     | row_idx = 2, row_idx % numRows - 1 = 2
I S H I | row_idx = 3, row_idx % numRows - 1 = 0
    R   | row_idx = 4, row_idx % numRows - 1 = 1
  I     | row_idx = 6, row_idx % numRows - 1 = 2
N G     | row_idx = 7, row_idx % numRows - 1 = 3


numRows = 5

P A Y P A | row_idx = 0, row_idx % numRows - 1 = 0
      L   | row_idx = 1, row_idx % numRows - 1 = 1
    I     | row_idx = 2, row_idx % numRows - 1 = 2
  S       | row_idx = 3, row_idx % numRows - 1 = 3
H I R I N | row_idx = 4, row_idx % numRows - 1 = 0
      G   | row_idx = 5, row_idx % numRows - 1 = 1


numRows = 6

P A Y P A L | row_idx = 0, row_idx % numRows - 1 = 0
        I   | row_idx = 1, row_idx % numRows - 1 = 1
      S     | row_idx = 2, row_idx % numRows - 1 = 2
    H       | row_idx = 3, row_idx % numRows - 1 = 3
  I         | row_idx = 4, row_idx % numRows - 1 = 4
N G         | row_idx = 5, row_idx % numRows - 1 = 0

"""
