class Solution:

    # apparently, python's heapq can be used with a list of lists as well,
    # it will sort based on the first element

    # submission right after looking at neetcode's solution
    # gave this a dry run, makes total sense!

    # this is Dijkstra's btw

    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        row_len, col_len = len(heights), len(heights[0])
        visited = set()

        # heap stores, minimum_absolute_difference, row, col
        heap = [[0, 0, 0]]

        while heap:
            diff, row, col = heapq.heappop(heap)
                
            if (row, col) == (row_len - 1, col_len - 1):
                return diff

            if (row, col) not in visited:
                visited.add((row, col))

                # max() because if you choose this path, you'll HAVE to incur that cost

                if row - 1 >= 0:
                    heapq.heappush(heap, [max(diff, abs(heights[row][col] - heights[row - 1][col])), row - 1, col])
                
                if col - 1 >= 0:
                    heapq.heappush(heap, [max(diff, abs(heights[row][col] - heights[row][col - 1])), row, col - 1])
                
                if row + 1 < row_len:
                    heapq.heappush(heap, [max(diff, abs(heights[row][col] - heights[row + 1][col])), row + 1, col])
                
                if col + 1 < col_len:
                    heapq.heappush(heap, [max(diff, abs(heights[row][col] - heights[row][col + 1])), row, col + 1])