class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        visited = set()
        for i in range(1, len(arr)-1):
            if i in visited: continue
            lp, rp = i-1, i+1
            if arr[lp] < arr[lp+1] > arr[rp]:
                while lp > 0 and arr[lp] > arr[lp-1]:
                    lp-= 1
                while rp < len(arr)-1 and arr[rp] > arr[rp+1]:
                    visited.add(rp)
                    rp+=1
                res = max(res, rp-lp+1)
        return res