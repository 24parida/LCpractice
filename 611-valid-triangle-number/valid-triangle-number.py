class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for c in range(len(nums)-1, 1, -1):
            l, r = 0, c-1
            while l < r:
                if nums[l] + nums[r] > nums[c]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        
        return count