class Solution:

    # even though I found this under the Neetcode 2D - DP section,
    # first, I am going to try a graph based approach
    # omg my BFS solution actually made sense and worked (at least on the initial 2x testcases)

    path_count = 0

    def bfs(self, r, c, m, n):

        if r == m - 1 and c == n - 1:
            self.path_count += 1
            return
        
        if r >= m or c >= n:
            return
        
        self.bfs(r + 0, c + 1, m, n)
        self.bfs(r + 1, c + 0, m, n)

    def uniquePaths(self, m: int, n: int) -> int:

        self.path_count = 0

        self.bfs(0, 0, m, n)

        return self.path_count