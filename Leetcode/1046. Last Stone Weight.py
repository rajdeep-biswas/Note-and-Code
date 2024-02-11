class Solution:

    # based on my understand of heaps / priority queues from /Leetcode/919 · Meeting Rooms II.py
    # also, /Leetcode/215. Kth Largest Element in an Array.py
    # and also help from https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
    # PS: I am sick of using the negatives
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            heaviest, heavy2nd = -heapq.heappop(heap), -heapq.heappop(heap)
            if heaviest > heavy2nd:
                newstone = heaviest - heavy2nd
            else:
                newstone = heavy2nd - heaviest
            heapq.heappush(heap, -newstone)
        
        if heap:
            return -heap[0]
        else:
            return 0