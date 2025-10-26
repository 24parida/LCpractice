class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)

        diffs = 0
        
        for elem in c1:
            if elem in c2:
                diffs += abs(c1[elem] - c2[elem])
            else:
                diffs += c1[elem]
        
        for elem in c2:
            if elem not in c1:
                diffs += c2[elem]
        
        return diffs // 2
        
