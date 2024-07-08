# You are given an n x n binary matrix grid where 1 represents land and 0 represents
#  water.
#  An island is a 4-directionally connected group of 1's not connected to any other 1's.
#  There are exactly two islands in the grid.
#  You may change 0's to 1's to connect the two islands to form one island.
#  Return the smallest number of 0's you must flip to connect the two islands.


# Example 1 : 

# Input Grid
# [[0,1]
# [1,0]]

# Output: 1
 
# Example-2: 
# Input Grid
 
# [[1,1,1]
#  [1,0,0]
#  [0,0,1]]

# Output: 1

"""
[
    1 1 1 1
    0 1 0 0
    0 1 0 0
    0 0 0 1
]

queue = [, (1, 0)]
(0, 0)
(0, 1)
"""

input = [[1,0,0], 
        
        
[1,0,0], [0,0,1]]

sr, rc = 0, 0

for r in range(len(input)):
    for c in range(len(input[r])):
        if input[r][c] == 1:
            sr, sc = r, c
            break
    if sr != 0 and sc != 0:
        break
        
# starts from sr, sc
island_a = {(sr, sc)}

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

queue = [(sr, sc)]

while queue:
    
    x, y = queue.pop()
    
    island_a.add((x, y))
    
    for dr, dc in directions:
        
        if x + dr in range(len(input)) and y + dc in range(len(input)):
            if input[x + dr][y + dc] == 1:
                island_a.add([x + dr, y + dc])
                queue.insert(0, (x + dr, y + dc))
    
min_distance = len(input) * len(input)

visited = island_a
queue = list(island_a)
       
distance_so_far = 0
    
while queue:
    
    x, y = queue.pop()
    
    visited.add((x, y))
    
    distance_so_far += 1
    
    for dr, dc in directions:
        
        if x + dr in range(len(input)) and y + dc in range(len(input)) and (x + dr, y + dc) not in visited:
            
            if input[x + dr][y + dc] == 1:
                break
            
            visited.add((x + dr, y + dc))
            queue.insert(0, (x + dr, y + dc))
    
    min_distance = min(min_distance, distance_so_far)

print(min_distance)