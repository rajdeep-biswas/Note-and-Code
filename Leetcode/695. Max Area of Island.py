class Solution:

    # this solution is very similar to (200. Number of Island), refer to that solution if the code does not make sense

    visited = None
    max_count = None
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def __init__(self):
        self.visited = set()
        self.max_count = 0

    def dfs(self, grid, r, c):
        count = 1
        q = []
        q.insert(0, (r, c))
        self.visited.add((r, c))

        while q:
            r, c = q.pop()
            for dr, dc in self.directions:

                i_r = r + dr
                i_c = c + dc

                if i_r in range(len(grid)) and \
                    i_c in range(len(grid[0])) and \
                    grid[i_r][i_c] == 1 and \
                    (i_r, i_c) not in self.visited:

                    q.insert(0, (i_r, i_c))
                    self.visited.add((i_r, i_c))
                    count += 1
        
        self.max_count = max(count, self.max_count)


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in self.visited:
                    self.dfs(grid, r, c)
        return self.max_count