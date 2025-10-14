class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s))]
        ## cats and dog
        # cat sand dog

        for i in range(len(s) -1, -1, -1):
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if i + len(word) < len(s):
                        for j in dp[i+len(word)]:
                            dp[i].append(word + " " + j)
                    else:
                        dp[i].append(word)
        
        return dp[0]

        # catsanddog
        # cat, and, dog

                
        