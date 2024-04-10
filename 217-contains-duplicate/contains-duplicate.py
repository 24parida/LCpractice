class Solution(object):
    def containsDuplicate(self, nums):
        a = set()
        for i in nums:
            if i in a: return True
            a.add(i)

        