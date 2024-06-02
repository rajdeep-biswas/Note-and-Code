
"""

Search in Rotated Sorted Array - LeetCode
https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1176221204/


 Given an array of integers that is sorted but rotated find the smallest element in the array
 For example {3, 5, 6, 1, 2} returns 1.

 Assume that the array does not have any duplicates.

def findMin(input):
    #todo: implement solution

    
     l     m     r
    {3, 5, 6, 1, 2}
    {5, 1, 2, 3, 4}
    
    
    l = 0
    r = len(input) - 1

    m = (l + r) // 2

    while l < r:

        if input[m] > input[l] and input[m] < input[r]:

            l = m
        
        else:

            r = m

    if m == len(input) - 1:
        return min(input[m], input[0])
    return min(input[m], input[m + 1])
"""

"""
Returns true if all tests pass. Otherwise returns false
"""
"""
def doTestsPass():
    ok = True
    tests = [
        (1, [3,4,5,6,1,2]),
        (1, [2,1]),
        (1, [1]),
        (1,[1,2,3,4,5]),
        (None,[])
    ]

    for (expected,testInput) in tests:
        result = findMin(testInput)
        if result == expected:
            print("Test passed for", testInput, "got", result, "for", expected,"\n")
        else:
            print("Test failed for", testInput, "got", result, "instead of", expected, "\n")
            ok = False
    return ok

if __name__ == "__main__":
    result = doTestsPass()

    if result:
        print("All tests pass\n")
    else:
        print("Tests fail\n")
        """
# 6 results are available, use up and down arrow keys to navigate.Smallest NumberPython





"""

Trapping Rain Water - LeetCode
https://leetcode.com/problems/trapping-rain-water/description/

 Instructions to candidate.
  1) Given an array of non-negative integers representing the elevations
     from the vertical cross section of a range of hills, determine how
     many units of snow could be captured between the hills. 

     See the example array and elevation map below.
                                 ___
             ___                |   |        ___
            |   |        ___    |   |___    |   |
         ___|   |    ___|   |   |   |   |   |   |
     ___|___|___|___|___|___|___|___|___|___|___|___
     [0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0]
                                 ___
             ___                |   |        ___
            |   | *   *  _*_  * |   |_*_  * |   |
         ___|   | *  _*_|   | * |   |   | * |   |
     ___|___|___|_*_|___|___|_*_|___|___|_*_|___|___
     [0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0]
              l   r
    
    max_so_far = 3
     total = 0
     cumulative = 1

    i: (maxl, maxr)


     Solution: In this example 13 units of snow (*) could be captured.

  2) Implement computeSnowpack() correctly.
  3) Consider adding some additional tests in doTestsPass().
"""

def computeSnowpack(arr):
    # TODO: Implement computeSnowpack

    total = 0

    for i in range(1, len(arr)):
        
        max_left = arr[i]
        max_right = arr[i]
        
        for j in range(1, len(arr)):

            if j < i and arr[j] > max_left:
                max_left = arr[j]
            
            elif j > i and arr[j] > max_right:
                max_right = arr[j]

        total += min(max_right, max_left) - arr[i]
    
    return total
            

def doTestsPass():
    """ Returns True if all tests pass. Otherwise returns False. """
    tests = [
            [[0,1,3,0,1,2,0,4,2,0,3,0], 13],
            # TODO: add more tests
            ]

    for test in tests:
        if not (computeSnowpack(test[0]) == test[1]):
            return False
    return True

if __name__ == "__main__":
    if( doTestsPass() ):
        print( "All tests pass" )
    else:
        print( "Not all tests pass" )
