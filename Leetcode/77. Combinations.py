class Solution:

    """
    this is my own solution coming from Neetcode's explanation and solution Leetcode/78. combinations.py
    on the contrary, neetcode's own solution with a loop inside the search method makes little sense to me. i am happy with my solution
    for basic understanding, check 78's comments. I have commented the diffs below
    """
    
    res = []
    combination = []

    def search(self, i, n, k):

        # base case if 1-based index has surpassed n
        if i > n:
            # also add combination to main list only if matches the desired length of k
            if len(self.combination) == k:
                self.res.append(self.combination.copy())
            
            # always return in either case
            return
        
        # the below recursive calls are the exact same as the 78 solution
        self.combination.append(i)
        self.search(i + 1, n, k)

        self.combination.pop()
        self.search(i + 1, n, k)


    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.res = []
        self.combination = []

        # start with 1 instead of 0 to make the code slightly more readable
        self.search(1, n, k)

        return self.res