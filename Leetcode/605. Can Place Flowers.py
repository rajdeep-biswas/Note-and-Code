class Solution:

    # update: I looked at Neetcode (youtube.com/watch?v=ZGxqqjljpUI)'s solution and agreeing to the comments there, it doesn't really make a lot of intuitive sense. I also disagree wiht the guy that it's actually a Medium problem, it is correctly placed at Easy.
    # The commenters also led me to the Leetcode editorial (leetcode.com/problems/can-place-flowers/editorial) solution, and I am delighted to note that it's similar in spirit to my solution, after I made some meaningful changes to it, documented below.

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        # got rid of checking 1-length edge cases. the conditionals within the loop take care of that. the 'how?' should be clear by the end

        for i in range(len(flowerbed)):

            # I had to move the first if condition to the top to take care of not running into a runtime index out of bounds error
            # it is super important that this condition should appear before the other two (even if they're if-else'd). the latter two ifs can be swapped around, however
            # for example, with the testcase {flowerbed = [0], n = 1}, the last bit flowerbed[i - 1] only works in a Pythonic way because of flowerbed[-1] resulting into the last index. this cannot work with flowerbed[i + 1], and that is how the edgecases involving len(flowerbed) == 1 are handled
            # I would recommend following the editorial solution for a more language-agnostic solution
            if i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] != 1:
                flowerbed[i] = 1
                count += 1
            if flowerbed[i] == 0 and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                flowerbed[i] = 1
                count += 1
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] != 1:
                flowerbed[i] = 1
                count += 1
        return n <= count