class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        m = {}
        m2 = {}
        for i in s1:
            m[i] = m.get(i, 0) + 1
        
        l, cor = 0, 0
        for r in range(len(s2)):
            if r-l+1 > len(s1):
                if s2[l] in m:
                    if m2.get(s2[l], 0) > m[s2[l]]: cor +=1
                    else: cor-=1
                m2[s2[l]] = m2.get(s2[l], 0) - 1
                l+=1
            if s2[r] in m:
                if m2.get(s2[r],0) < m[s2[r]]: cor +=1
                else: cor-=1
                m2[s2[r]] = m2.get(s2[r],0) + 1
            print(cor)
            if cor == len(s1): return True

        return False
        