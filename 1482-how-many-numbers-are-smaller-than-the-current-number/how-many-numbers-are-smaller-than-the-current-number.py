class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        res_d = {}
        for x, i in enumerate(temp):
            if i not in res_d:
                res_d[i] = x

        res = [0] * len(nums)
        for x, i in enumerate(nums):
            res[x] = res_d[i]

        return res

        

        