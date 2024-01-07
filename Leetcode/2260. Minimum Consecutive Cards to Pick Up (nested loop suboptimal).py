class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        # found this looking at an older contest (leetcode.com/contest/weekly-contest-291), submitting a suboptimal solution for practice

        index_dict = {}

        for i in range(len(cards)):
            if cards[i] in index_dict:
                index_dict[cards[i]].append(i)
            else:
                index_dict[cards[i]] = [i]

        spaces = []

        for item in index_dict:
            if len(index_dict[item]) > 1:

                # this inner loop addresses the case that there might be more than two of the same cards
                for i in range(len(index_dict[item]) - 1):
                    spaces.append(index_dict[item][i + 1] - index_dict[item][i] + 1)

        return min(spaces) if spaces else -1