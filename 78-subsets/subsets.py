class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur, res = [], []
        def backtrack(idx):
            if idx == len(nums):
                res.append(cur[:])
                return
            
            cur.append(nums[idx])
            backtrack(idx+1)
            cur.pop()
            backtrack(idx+1)
        backtrack(0)
        return res
        