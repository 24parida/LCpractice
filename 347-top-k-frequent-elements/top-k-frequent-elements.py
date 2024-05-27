class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
        
        for i in count:
            arr[count[i]].append(i)
        
        print(arr)

        res = []
        for i in arr[::-1]:
            if len(i) != 0:
                for j in i: 
                    res.append(j)
                    if len(res) == k: return res

        return []

        
        