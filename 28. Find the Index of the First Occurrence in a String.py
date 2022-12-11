class Solution:
    """
    This a a crude solution (even though it meets all LC testcases). According to Diptesh da, a KMP implementation is necessary to learn.
    """
    def strStr(self, haystack: str, needle: str) -> int:

        # flag variable for the beginning index where needle was found; also doubles as a resetting mechanism
        found = -1
        # two index pointers pointing to haystack and needle arrays, respectively
        h_i = 0
        n_i = 0

        while h_i < len(haystack):

            if haystack[h_i] == needle[n_i]:
                if n_i == 0:
                    # if match is found, set found to be the same index as haystack
                    found = h_i

                # increment needle pointer
                n_i += 1

            # if match is not found (or was never found), reset n_i to beginning and set found to negative
            else: # can also be replaced with condition `elif found >= 0:` so as to execute this block ONLY when a non-match is found AFTER a match
                if n_i != 0:
                    # also reset haystack pointer to be that at the last "found" index (to be incremented by one at the end of the loop)
                    h_i = found
                n_i = 0
                found = -1

            # if all of needle has been found, we have our match
            if n_i == len(needle):
                break
            h_i += 1

        # if we have run out of haystack and yet didn't find all of needle (found still remains > -1)
        if n_i != len(needle):
            found = -1
    
        return found