class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        values = set()

        for i in nums:
            if i in values:
                return True
            else:
                values.add(i)
        return False