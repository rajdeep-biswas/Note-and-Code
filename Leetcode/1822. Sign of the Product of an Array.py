class Solution:
    def arraySign(self, nums: List[int]) -> int:

        # smartass solution instead of multiplying
        
        count_negs = 0
        
        for num in nums:

            if num == 0:
                return 0
            
            if num < 0:
                count_negs += 1
        
        return -1 if count_negs % 2 else 1