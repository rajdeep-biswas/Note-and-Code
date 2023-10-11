class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        # low effort streak solution

        balloon = "balloon"
        balloon_dict = {}

        for l in balloon:
            balloon_dict[l] = 0
        
        for l in text:
            if l in balloon_dict:
                balloon_dict[l] += 1
        
        # this is the only big brain part
        return min(balloon_dict.values())