# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         s = set(nums)
#         best = float('-inf')
#         for num in nums:
#             if num + 1 not in s:
#                 curr = 1
#                 curr_num = num - 1
#                 while curr_num in s:
#                     curr += 1
#                     curr_num -= 1
#                 best = max(curr, best)
        
#         return best
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for num in s:  # iterate over set directly
            if num - 1 not in s:  # start of a sequence
                curr = 1
                curr_num = num + 1
                while curr_num in s:
                    curr += 1
                    curr_num += 1
                best = max(best, curr)

        return best
