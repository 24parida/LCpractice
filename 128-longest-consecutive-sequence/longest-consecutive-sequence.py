class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)
        best = float('-inf')
        for num in s:
            if num + 1 not in s:
                curr = 1
                curr_num = num - 1
                while curr_num in s:
                    curr += 1
                    curr_num -= 1
                best = max(curr, best)
        
        return best
        