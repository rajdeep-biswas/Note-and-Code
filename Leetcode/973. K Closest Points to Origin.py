class Solution:

    # min heap solution so thank fuck i don't have to use the negatives anymore
    # context: Leetcode/1046. Last Stone Weight.py

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        points_dict = {}

        for x, y in points:

            # dfo is distance from origin
            dfo = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)

            heapq.heappush(heap, dfo)
            if dfo not in points_dict:
                points_dict[dfo] = [[x, y]]
            else:
                points_dict[dfo].append([x, y])

        res = []

        # this part took me a few shots
        while k:
            for coords in points_dict[heapq.heappop(heap)]:
                res.append(coords)
                k -= 1

        return res