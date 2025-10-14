class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_words_set = set(["".join(sorted(i)) for i in startWords])

        res = 0
        for t in targetWords:
            t = "".join(sorted(t))

            for i in range(len(t)):
                if t[:i] + t[i+1:] in start_words_set:
                    res += 1
                    break
        
        return res
