class Solution:

    # slightly changed approach by "returning" path value instead of incrementing class variable
    # and the original is also completely my own approach /Leetcode/non-solutions/62. Unique Paths (TLE).py
    # trying out a caching mechanism based on my understanding

    cache = dict()

    def bfs(self, r, c, m, n, count):

        res = 0

        # cache hit
        if (r, c) in self.cache:
            return self.cache[(r, c)]

        # if we have landed at goal, return "one more count"
        if r == m - 1 and c == n - 1:
            return count + 1
        
        # if out of bounds, no path
        if r >= m or c >= n:
            return 0
        
        # add to result value and cache to current (r, c) and not (r, c + 1)
        res += self.bfs(r, c + 1, m, n, count)
        self.cache[(r, c)] = res

        # add to result value and cache to current (r, c) and not (r + 1, c)
        res += self.bfs(r + 1, c, m, n, count)
        self.cache[(r, c)] = res

        return res


    def uniquePaths(self, m: int, n: int) -> int:

        self.cache = dict()

        # start looking from origin (0, 0) and also have found 0 paths so far
        return self.bfs(0, 0, m, n, 0)