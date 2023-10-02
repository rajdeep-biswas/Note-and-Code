class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # this does not really belong in non-solutions/ since it does get accepted and is also O(N) as the spec asks. just putting it here for the interesting story
        # solution from fuck knows when. it was just left half done, here, in the editor saved on cloud. never been submitted before. i had to write line 17 and 18 (and comment out line 15 lol) before submitting on 2nd oct 2023
        dic_count = {0: 0, 1: 0, 2: 0}
        for item in nums:
            dic_count[item] += 1
        
        st = ''
        for item in dic_count:
            st += str(item) * dic_count[item]
        # [0,0,2,1,1,2]
        
        for i in range(len(st)):
            nums[i] = int(st[i])

        # this problem looks awfully familiar - leetcode IDE had a cloud saved half-done solution I had written from fuck knows when. The Submissions tab is empty - I never even finished attempting it. Creepy thing is I distinctly remember someone telling me / having read a 2-pointer approach but can't for the life of me figure out who / where from / when. Best guess is that it was probably in a pre-incorporation mock interview. And the fact that I am not able to instantly code up "the solution that made so much intuitive sense to me" is making me want to pull hair out. This is the second problem I am hard stuck on, since today afternoon.