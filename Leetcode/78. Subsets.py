class Solution:

    # neetcode's solution (slightly modified to my taste of object oriented)

    res = []
    subset = []

    # heavily tweaked version of DFS. we *are* using a tree-like branching structure but we're not thinking in the left / right children subtree recursion mindset anymore
    def dfs(self, nums, i, numlen):

        # if we have surpassed array length, we stop looking and append the existing subset to main results
        if i >= numlen:
            # note that i not only serves the purpose of an index (to figure which element to look at) but also a marker of when to append the subset to the main list every time we desire to account for a [smaller] subset
            self.res.append(self.subset.copy()) # we should use .copy() of a list since keeping the self.subset in the res will reflect all changes made to it
            return

        # the decision of including the ith element
        self.subset.append(nums[i])
        self.dfs(nums, i + 1, numlen) # and subsequent recursion

        # the decision of _not_ including the ith element
        self.subset.pop()
        self.dfs(nums, i + 1, numlen) # and subsequent recursion

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        self.subset = []

        self.dfs(nums, 0, len(nums))

        return self.res