class Solution:

    # easy problem, have solved similar before, but thought it was a nice rep(etition)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0
        right, down, left, up = [0, 1], [1, 0], [0, -1], [-1, 0]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    contrib = 4
                    if i > 0:
                        if grid[i + up[0]][j + up[1]] == 1:
                            contrib -= 1
                    if i < len(grid) - 1:
                        if grid[i + down[0]][j + down[1]] == 1:
                            contrib -= 1
                    if j > 0:
                        if grid[i + left[0]][j + left[1]] == 1:
                            contrib -= 1
                    # I had missed a bug on this line. using len(grid) instead of len(grid[i]) has it working only for square grids. rectangular ones might fail. feel good about the quick debug i made
                    if j < len(grid[i]) - 1:
                        if grid[i + right[0]][j + right[1]] == 1:
                            contrib -= 1
                    perim += contrib
        return perim