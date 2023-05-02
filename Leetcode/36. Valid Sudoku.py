class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # brute force esque solution of checking each row for all columns, each column for all rows, and finally each ninths (quadrants of nines)

        # check columns
        for i in range(9):
            counts = [0] * 9
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    counts[int(num) - 1] += 1
            for count in counts:
                if count > 1:
                    return False

        # check rows
        for i in range(9):
            counts = [0] * 9
            for j in range(9):
                num = board[j][i]
                if num != '.':
                    counts[int(num) - 1] += 1
            for count in counts:
                if count > 1:
                    return False

        # check ninths
        # figured out the offsets for each 3x3 scan
        inits = [
            [0, 0], [0, 3], [0, 6],
            [3, 0], [3, 3], [3, 6],
            [6, 0], [6, 3], [6, 6]
        ]

        for x, y in inits:
            counts = [0] * 9
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    num = board[j][i]
                    if num != '.':
                        counts[int(num) - 1] += 1
            for count in counts:
                if count > 1:
                    return False

        return True