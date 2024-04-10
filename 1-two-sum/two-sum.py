class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sol = set()
        for x, y in enumerate(nums):
            if target-y in sol: 
                return [x, [i for i in range(len(nums)) if nums[i] == target-y][0]]
            else: sol.add(y)
        