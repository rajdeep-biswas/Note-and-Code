class Solution:

    # so this is my ugly O(n) solution with a ton of if conditions
    # just submitting here to mark me retuning to DSA after ~10 days, and also to compare needcode's solution
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if len(flowerbed) == 1:
            if n >= 1:
                return flowerbed[0] == 0
            else:
                return True
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] != 1:
                flowerbed[i] = 1
                count += 1
            if i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] != 1:
                flowerbed[i] = 1
                count += 1
            if flowerbed[i] == 0 and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                flowerbed[i] = 1
                count += 1
        return n <= count