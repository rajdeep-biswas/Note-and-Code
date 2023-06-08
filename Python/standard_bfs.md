Algorithm -
- initiate empty `queue`.
- `enqueue` initial coordinates.
- add coordinates to `visited` set.
- while `queue` is not empty:
     - `dequeue` and store coordinates (r, c).
     - `for each direction`
        - add direction to each (r, c).
        - if following conditions are met:
            - r is in the range of `row_length`
            - c is in the range of `col_length`
            - (r, c) not already in `visited`
            - // any additional condition specific to usecase
        - then do as follows:
            - `enqueue` (r, c)
            - add (r, c) to `visited` set
            - // any additional operations specific to usecase
         


```python
def bfs(self, grid, r, c):
        # area = 0
        q = []
        q.insert(0, (r, c))
        self.visited.add((d_r, d_c))

        while q:
            r_i, c_i = q.pop()
            
            for dr, dc in self.directions:
                d_r = r_i + dr
                d_c = c_i + dc

                if (d_r, d_c) not in self.visited and \
                    d_r in range(len(grid)) and \
                    d_c in range(len(grid[0])) and \
                    grid[d_r][d_c] == 1:

                    # area += 1
                    q.insert(0, (d_r, d_c))
                    self.visited.add((d_r, d_c))

        return area
```