class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        lp = rp = 0
        if nums[lp] >= target: return 1
        add = nums[lp]
        
        while lp <= rp and rp < len(nums):
            while add < target and rp < len(nums):
                rp += 1
                if rp < len(nums):
                    add+= nums[rp]
            if add >= target:
                res = min(res, rp-lp+1)
                add-= nums[lp]
                lp += 1
           
        return res if res != float('inf') else 0
            
