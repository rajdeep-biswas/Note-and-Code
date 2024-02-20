class Solution:

    # watched neetcode's improvement over this, he does two searches. once starting from pacific nodes, to discover all the nodes that can get there. and a similar second starting from the atlantic ones
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row_len, col_len = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        pacific_nodes = []
        atlantic_nodes = []
    
        # pacific search
        for i in range(row_len):
            pacific_nodes.append([i, 0])
            atlantic_nodes.append([i, col_len - 1])
        
        # atlantic search
        for i in range(col_len):
            pacific_nodes.append([0, i])
            atlantic_nodes.append([row_len - 1, i])

        for row, col in pacific_nodes:
            stack = []
        
            stack.append([heights[row][col], row, col])
            while stack:
                height, r, c = stack.pop()
                pacific.add((r, c))
                for direction in directions:
                    r_prime, c_prime = r + direction[0], c + direction[1]

                    # if where we're about to step, is within range of the grid AND is the same or lower height as current cell, we add that cell to our search
                    if r_prime in range(0, row_len) and c_prime in range(0, col_len) and heights[r_prime][c_prime] >= heights[r][c] and (r_prime, c_prime) not in pacific:
                        stack.append([heights[r_prime][c_prime], r_prime, c_prime])
        
        for row, col in atlantic_nodes:
            stack = []
            stack.append([heights[row][col], row, col])
            while stack:
                height, r, c = stack.pop()
                atlantic.add((r, c))
                for direction in directions:
                    r_prime, c_prime = r + direction[0], c + direction[1]

                    # if where we're about to step, is within range of the grid AND is the same or lower height as current cell, we add that cell to our search
                    if r_prime in range (0, row_len) and c_prime in range(0, col_len) and heights[r_prime][c_prime] >= heights[r][c] and (r_prime, c_prime) not in atlantic:
                        stack.append([heights[r_prime][c_prime], r_prime, c_prime])

        return pacific.intersection(atlantic)