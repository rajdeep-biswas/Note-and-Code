class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # seemed to be an easy problem I just picked up for an easy daily-streak
        # but getting an O(n) solution seemed to be pretty involved

        # the last element is the "biggest" element to the right (since it's the only one so far)
        biggest = arr[len(arr) - 1]

        # iterate backwards starting from the 2nd last element
        for i in range(len(arr) - 2, -1, -1):

            # we need a swapping mechanism here to backup the ith index, set it to the biggest element (which may or may not be the same value as the current index), and set biggest to the bigger element of what *was* there at i (now in temp) and the current biggest element
            temp = arr[i]
            arr[i] = biggest
            biggest = max(temp, biggest)
            
        # set last element to -1 (this is always the case)
        arr[len(arr) - 1] = -1

        # in-place, baby!
        return arr

        """
        I didn't even want to attempt the O(n^2) because I have grown past doing that lol.
        For the O(n) solution, I did start to think of iterating the array backwards and keeping track of the biggest-so-far element. Which was validated by the following comment in Discussion -
        rammanoj | Mar 11, 2023
        Hint:
        A lot of approaches comes into mind... but this could be solvable in O(n) time and O(1) space.

        Try to think in reverse manner i.e. computing values from the end of the array instead of start.
        """