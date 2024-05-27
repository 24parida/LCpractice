class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m = {}
        res = 0

        for i in nums:
            m[i] = i-1

        for r in nums:
            if m[r] in m: continue
            curRes = 1
            temp = r
            while temp+1 in m:
                curRes += 1
                temp+=1
            res = max(curRes, res)

        return res



    
        

