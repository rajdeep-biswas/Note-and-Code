class Solution:
    """
    Lookback.
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # initializing i for traversing nums1 and j for traversing nums2.
        # (the latter also comes in handy later to determine where to begin putting in the rest of the elements)
        i = j = 0

        # make sure you do not index error on either nums1 or nums2
        while i < len(nums1) and j < n:

            # if nums2 has an element smaller than ith nums1 element, squeeze that in
            if nums2[j] < nums1[i]:

                # set k to last element of nums1
                k = len(nums1) - 1

                # copy elements rightwards until you reach i; which is where you want to squeeze in the smaller element
                while k > i:
                    nums1[k] = nums1[k - 1]
                    k -= 1

                # actually squeeze in the intended element
                nums1[i] = nums2[j]

                # at end move j pointer forward since you don't need to deal with that element anymore
                j += 1

            # if element is larger, it means nums1 already has index element in place, move forward.
            else:
                i += 1

        # (this was the part I was stuck the longest at)
        # m is the number of elements in the first array initially and j is the count of elements you have already squeezed in / displaced
        # so you just put in rest of the elements from nums2 (starting from index j) into nums1 (starting from index m + j)
        i = m + j

        while i < len(nums1):
            nums1[i] = nums2[j]
            i += 1
            j += 1