class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {
        }

        for x, i in enumerate(nums):
            if target-i in values:
                return (x, values[target - i])
            else:
                values[i] = x