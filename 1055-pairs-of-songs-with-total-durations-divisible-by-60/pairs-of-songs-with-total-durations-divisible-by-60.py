class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        m = collections.defaultdict(list)
        res = 0
        for i in time:
            key = (60 - (i % 60)) % 60
            if key in m:
                res += len(m[key])
            m[i % 60].append(i)

        return res


        