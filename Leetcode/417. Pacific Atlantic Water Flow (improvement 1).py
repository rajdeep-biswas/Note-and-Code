class Solution:

    # pen and papered the whole thing
    # my "path optimization" didn't work, right now this is inefficient af but I am very happy that it does work
    # my initial thoughts were that this problem needed a priority queue (like 1631. Path With Minimum Effort) but that didn't feel necessary
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row_len, col_len = len(heights), len(heights[0])
        res = []

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # brute force by searching floodfill from every node
        for row in range(row_len):
            for col in range(col_len):
                
                # flag variables to check starting from [row, col], if it's possible to reach BOTH the oceans
                pacific, atlantic = False, False
                # path = []

                # and stack + visited set initialization for standard bfs
                stack = []
                visited = set()

                stack.append([heights[row][col], row, col])

                while stack:
                    height, r, c = stack.pop()

                    if (r, c) in visited:
                        continue
                    
                    visited.add((r, c))

                    # check if current search manages to find r, c values which reach either of the oceans
                    if r == 0 or c == 0:
                        pacific = True
                    if r == row_len - 1 or c == col_len - 1:
                        atlantic = True
                    
                    # if by the of search, we have managed to reach both the oceans, the original starting point should be counted
                    if pacific and atlantic:
                        # path.append()
                        res.append((row, col))
                        # and we can also break out of the current loop early, which strongly boosts runtime. this "break" alone boosted from ~6400ms to 2000ms
                        # also this improvement alone fixed the issue that res was getting multiple copies of the same origin value
                        break
                    
                    for direction in directions:
                        r_prime, c_prime = r + direction[0], c + direction[1]

                        # if where we're about to step, is within range of the grid AND is the same or lower height as current cell, we add that cell to our search
                        if r_prime in range (0, row_len) and c_prime in range(0, col_len) and heights[r_prime][c_prime] <= heights[r][c]:
                            stack.append([heights[r_prime][c_prime], r_prime, c_prime])
                            # path.append([r_prime, c_prime])

        return res