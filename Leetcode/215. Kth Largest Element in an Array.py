class Solution:

    # based on my understand of heaps / priority queues from /Leetcode/919 · Meeting Rooms II.py
    # and also help from https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
    # I am not entirely sure if this counts as O(N)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])

        for i in range(k):
            last = -heapq.heappop(heap)

        return last