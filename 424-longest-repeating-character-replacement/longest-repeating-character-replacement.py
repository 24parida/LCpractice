class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = [0] * 26
        res, l = 0, 0
        curMax = -1

        for r in range(len(s)):
            cnt[ord(s[r].lower()) - ord('a')] += 1
            curMax = max(cnt[ord(s[r].lower()) - ord('a')], curMax)

            while (r-l+1 - curMax) > k:
                cnt[ord(s[l].lower()) - ord('a')] -= 1
                l += 1

            res = max(res, r-l+1)
        
        return res
            
        