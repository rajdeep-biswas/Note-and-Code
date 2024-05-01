class Solution:

    # not a lot to comment. just posting it because Subbooh asked me to solve this
    # the 4-directional search pretty intuitive at this point
    # see Number of Islands, etc., if it's not making sense by any chance

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        target_color = image[sr][sc]

        visited = set()

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        queue = []

        queue.insert(0, (sr, sc))

        while queue:

            sr, sc = queue.pop()

            if (sr, sc) not in visited:
                visited.add((sr, sc))

                # if image[sr][sc] == target_color:
                image[sr][sc] = color
                
                for dr, dc in directions:
                    if sr + dr in range(len(image)) and sc + dc in range(len(image[0])) and image[sr + dr][sc + dc] == target_color:
                        queue.insert(0, (sr + dr, sc + dc))
        
        return image