class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # using a defaultdict instead of a regular dict just to avoid one edge case of appending strings to a list without a key
        grouped_dict = defaultdict(list)

        # go through each string
        for st in strs:

            # populate a alphabet frequency array
            idxs = [0] * 26
            for letter in st:
                idxs[ord(letter) - ord('a')] += 1

            # use said frequency array as a tuple key to holding a list of all anagrams
            grouped_dict[tuple(idxs)].append(st)

        return grouped_dict.values()