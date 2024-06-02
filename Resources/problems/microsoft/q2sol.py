# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 2384. Largest Palindromic Number (leetcode)
# https://github.com/doocs/leetcode/blob/main/solution/2300-2399/2384.Largest%20Palindromic%20Number/README_EN.md
# https://leetcode.com/problems/largest-palindromic-number/

import itertools

def isPalindrome(S):
    return S == S[::-1]

def solution(S):

    # get all possible permutations of the string, of all lengths
    all_permutations = []
    for i in range(1, len(S)+1):
        all_permutations.extend(itertools.permutations(S, i))

    max_res = 0

    # go through each permutation, check if it's a palindrome, doesn't have a leading zero and is greater than current maximum found result
    for perm in all_permutations:
        perm = ''.join(perm)
        if isPalindrome(perm) and perm[0] != '0' and int(perm) > max_res:
            max_res = int(perm)
    
    return str(max_res)