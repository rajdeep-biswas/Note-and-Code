class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # initialize m to point at last populated element of nums1, n to last element of nums2, and k to last element of nums1 (most cases, a zero)
        m = m - 1
        n = n - 1
        k = len(nums1) - 1

        # do one passthrough to compare pairs of elements and put them at the end of nums1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1
            k -= 1

        # merge any remaining elements in nums1, or nums2 (it's never both because the above loop covers at least either one)
        while m >= 0:
            nums1[k] = nums1[m]
            k -= 1
            m -= 1
        
        while n >= 0:
            nums1[k] = nums2[n]
            k -= 1
            n -= 1
