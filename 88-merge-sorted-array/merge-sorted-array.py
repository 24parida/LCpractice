class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r, p = m - 1, n - 1, m + n - 1
        while r >= 0:
            if l >= 0 and nums1[l] >= nums2[r]:
                nums1[p] = nums1[l]
                l -= 1
            else:
                nums1[p] = nums2[r]
                r -= 1
            p -= 1
        


        