class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # O(n) space and time solution. don't understand what all the fuss in the Discussion was about, probably they have improved the problem since

        # record sums into array traversing from left to right
        sum_left = []
        total = 0
        
        for num in nums:
            
            sum_left.append(total + num)
            total += num
        
        # record sums into array traversing from right to left
        sum_right = []
        total = 0

        for num in nums[::-1]:

           sum_right.append(total + num)
           total += num

        # this needs reversing because it has appended in the reverse order
        sum_right = sum_right[::-1]
        
        # check for leftmost matching index, return index if found
        for i in range(len(nums)):

            if sum_left[i] == sum_right[i]:
                return i
        
        # return -1 if not found
        return -1