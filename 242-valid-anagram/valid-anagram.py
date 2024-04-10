class Solution(object):
    def isAnagram(self, s, t):

        d = {}

        for i in s:
            if i in d: d[i] += 1
            else: d[i] = 1

        for i in t:
            if i not in d: return False
            d[i] -= 1
            if d[i] < 0: return False

        for i in d:
            if d[i] != 0: return False

        return True

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        