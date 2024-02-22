class Solution:

    # attempt after looking at neetcode's explanation and solution
    # it's gonna take a multi-source BFS
    # and BFS isn't achieved simply by changing from stack to queue. the behavior is significantly changed with an additional nested inner loop

    def orangesRotting(self, grid: List[List[int]]) -> int:

        rowlen, collen = len(grid), len(grid[0])
        time, fresh = 0, 0
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        q = deque()

        # get a count of fresh oranges and also populate the queue based on the intial rotten oranges
        for r in range(rowlen):
            for c in range(collen):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        # if queue runs out or all fresh oranges have rotten
        while q and fresh > 0:

            # run breadth-first across all of the current rotten oranges
            for i in range(len(q)):
                r, c = q.popleft()

                for d in directions:
                    dr = r + d[0]
                    dc = c + d[1]

                    # if delta in range and is a fresh orange
                    if 0 <= dr < rowlen and 0 <= dc < collen and grid[dr][dc] == 1:

                        # orange becomes rotten and proceeds to get on the queue
                        grid[dr][dc] = 2
                        fresh -= 1
                        q.append([dr, dc])
            time += 1
        
        return -1 if fresh else time