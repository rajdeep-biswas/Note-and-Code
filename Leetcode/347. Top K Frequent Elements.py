class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # the neetcode guy did mention a (less efficient) solution with heapify - which might be a concept i'd want to learn sooner or later
        # https://www.youtube.com/watch?v=YPTqKIgVk-k

        # conventional frequency hashmap
        freq_dict = dict()
        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)

        # counter array the same length as original array.
        # note that it's important to initialize sublists in this manner instead of [[]] * (len(nums) + 1): check TIL 26th Apr Python
        count = [[] for i in range(len(nums) + 1)]

        # index will serve as the frequency and item will be sub-lists of all items that occur at that frequency
        for key in freq_dict:
            count[freq_dict[key]].append(key)

        # results array populated in reverse, loop exits as soon as length of res expands to match k - which is the desired number of _most frequent elements_
        res = []
        for i in range(len(count) - 1, 0, -1):
            for item in count[i]:
                res.append(item)
                if len(res) == k:
                    return res