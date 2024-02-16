class Solution:

    # pen and papered the whole thing
    # my "path optimization" didn't work, right now this is inefficient af but I am very happy that it does work
    # the issue right now is that line 38 is appending the same value multiple times, and I needed to inelegantly use a set() at the end to get unique results

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row_len, col_len = len(heights), len(heights[0])
        res = []

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for row in range(row_len):
            for col in range(col_len):
                
                pacific, atlantic = False, False
                stack = []
                stack.append([heights[row][col], row, col])
                path = []
                visited = set()

                while stack:
                    height, r, c = stack.pop()

                    if (r, c) in visited:
                        continue
                    
                    visited.add((r, c))

                    if r == 0 or c == 0:
                        pacific = True
                    if r == row_len - 1 or c == col_len - 1:
                        atlantic = True
                    
                    if pacific and atlantic:
                        # path.append()
                        res.append((row, col))
                    
                    for direction in directions:
                        r_prime, c_prime = r + direction[0], c + direction[1]

                        if r_prime in range (0, row_len) and c_prime in range(0, col_len) and heights[r_prime][c_prime] <= heights[r][c]:
                            stack.append([heights[r_prime][c_prime], r_prime, c_prime])
                            # path.append([r_prime, c_prime])
        

        # this is the most inelegant part of the code but I managed to significantly improve with Leetcode/417. Pacific Atlantic Water Flow (improvement 1).py
        results = []
        for item in list(set(res)):
            results.append(item)

        return results