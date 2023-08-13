class Solution:

    # Easy problem but I think this is my first greedy solution
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        # sorting seems necessary
        g = sorted(g)
        s = sorted(s)

        gi, si = 0, 0

        # note that count variable is redundant, if you just return gi at the end, that's the exact same value. all occurrences of count can be removed
        count = 0

        while gi < len(g) and si < len(s):

            # if current kid's greed level (lowest compared to ones on the right) is satisfied, we move on to the next kid and also the cookie gets consumed (move both child and cookie pointers, the latter happens either way)
            if g[gi] <= s[si]:
                count += 1
                gi += 1

            # if the kid isn't satisfied, we stay at the same kid and just try to find a bigger cookie for the brat (just move the cookie pointer)
            si += 1

        return count