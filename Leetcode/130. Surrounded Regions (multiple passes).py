class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # tried my own solution. will explain if it gets accepted
        # update: it did
        # the idea is to take all edge Os and convert them into placeholder P variables
        # now this combines things I learned from pacific atlantic water flow & rotting oranges
        # I do a DFS starting from each edge O (which are Ps after the first conversion), and "infect" all neighboring Os to become Ps as well
        # so these Ps are actually the (only) Os that CANNOT be converted to Xs, because we've found them coming in from edges
        # after this is done, we convert all survivor Os to Xs because they're the elligible ones (for the lack of a better word)
        # after that is done, we convert all Ps back to Os now that their job is done
        # good news is 114ms sounds like fantastic runtime, as well, it managed to beat 88% users 
        
        # edge passes to replace boundary 'O's with placeholders
        rowlen, collen = len(board), len(board[0])
        ps_stack = []

        # check along left and right
        for i in range(rowlen):
            if board[i][0] == 'O':
                board[i][0] = 'P'
                ps_stack.append([i, 0])
            if board[i][collen - 1] == 'O':
                board[i][collen - 1] = 'P'
                ps_stack.append([i, collen - 1])
        
        # check along bottom and top
        for i in range(collen):
            if board[0][i] == 'O':
                board[0][i] = 'P'
                ps_stack.append([0, i])
            if board[rowlen - 1][i] == 'O':
                board[rowlen - 1][i] = 'P'
                ps_stack.append([rowlen - 1, i])
        
        # start from each edge 'P' and convert all neighboring 'O's to 'P's
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()

        while ps_stack:
            row, col = ps_stack.pop()
            visited.add((row, col))
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rowlen and 0 <= c < collen and board[r][c] == 'O':
                    board[r][c] = 'P'
                    ps_stack.append([r, c])
        
        # final pass to replace all remaining Os with Xs and Ps back with Os
        for r in range(rowlen):
            for c in range(collen):
                if board[r][c] == 'P':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'