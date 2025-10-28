class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        sums = collections.defaultdict(int)
        res = float('-inf')
        for i in range(len(energy)-1, -1, -1):
            sums[i%k] += energy[i]
            res = max(res, sums[i%k]) 

        return res
        