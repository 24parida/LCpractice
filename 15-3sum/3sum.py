class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for x, i in enumerate(nums):
            target = 0 - i
            seen = set()
            for j in nums[x+1:]:
                if target - j in seen:
                    sol = sorted([i, j, target-j])
                    res.add(tuple(sol))
                else:
                    seen.add(j)
        
        return list(res)

        