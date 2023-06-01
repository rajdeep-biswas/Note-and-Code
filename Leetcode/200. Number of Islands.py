class Solution:
    # idea is to maintain a set of already visited spots to check if it's a part of an already counted island
    visited = set()

    # only four directions are necessary since diagonally attached spots are considered two separate islands
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self):
        self.visited = set()

    # standard(?) DFS implementation accounting for two dimensions
    # centrally flood fills and tracks all of the land boxes on an island, so that O(1) decisions can be taken on whether visited or not
    def dfs(self, grid, r, c):
        q = []
        q.insert(0, (r, c)) # queue, if you're going for BFS
        # q.append((r, c)) # stack, if you're going for DFS
        self.visited.add((r, c))
        while q:
            r, c = q.pop()
            for dr, dc in self.directions:
                # using an extra variable to preserve original position
                r_i = r + dr
                c_i = c + dc
                if  (r_i, c_i) not in self.visited and \
                    r_i in range(len(grid)) and \
                    c_i in range(len(grid[0])) and \
                    grid[r_i][c_i] == '1':

                    self.visited.add((r_i, c_i))
                    q.insert(0, (r_i, c_i)) # queue
                    # q.append((r_i, c_i)) # stack

    def numIslands(self, grid: List[List[str]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        count = 0
        for r in range(nrows):
            for c in range(ncols):
                # if current block is land ('1') and hasn't already been visited, by loop for by D/BFS, count it as a new island and add it to visited, then dfs on it to explore all of the island
                if grid[r][c] == '1' and (r, c) not in self.visited:
                    count += 1
                    self.dfs(grid, r, c)
        return count