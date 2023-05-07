class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # note that the vanilla solution for twoSum entirely works for all testcases on this, however, i think the idea here is to move on to a two-pointer solution
        low = 0
        high = len(numbers) - 1

        while low < high:
            # conditions should look pretty intuitive, if not watch first two minutes of youtube.com/watch?v=cQ1Oz4ckceM&t=67s
            if numbers[low] + numbers[high] == target:
                return [low + 1, high + 1]
            elif numbers[high] > target - numbers[low]:
                high -= 1
            else:
                low += 1