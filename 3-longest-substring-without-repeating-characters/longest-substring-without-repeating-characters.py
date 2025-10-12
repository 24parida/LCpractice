class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        best = float('-inf')
        l = 0
        counts = set()

        for r in range(len(s)):
            if s[r] in counts:
                while s[l] != s[r]:
                    counts.remove(s[l])
                    l += 1
                counts.remove(s[l])
                l += 1
            
            counts.add(s[r])
            curr = r - l + 1
            best = max(curr, best)

        return best

        