class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l = 0
        
        max_length = 0
        for r in range(len(s)):
            if s[r] in visited:
                while s[l] != s[r]:
                    visited.remove(s[l])
                    l += 1
                l += 1

            visited.add(s[r])
            max_length = max(max_length, r-l + 1)
        
        return max_length