class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = collections.defaultdict(int)
        res = 0
        l = 0
        maxF = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            maxF = max(counts[s[r]], maxF)
            while r - l + 1 - maxF > k:
                counts[s[l]] -= 1
                l += 1

        res = max(r-l+1, res)

        return res