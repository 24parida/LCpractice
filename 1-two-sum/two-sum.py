class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        val = {}


        for x, y in enumerate(nums):
            if target-y in val: return [x, val[target-y]]
            val [y] = x

        