class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
              2: ["a", "b", "c"]
            , 3: ["d", "e", "f"]
            , 4: ["g", "h", "i"]
            , 5: ["j", "k", "l"]
            , 6: ["m", "n", "o"]
            , 7: ["p", "q", "r", "s"]
            , 8: ["t", "u", "v"]
            , 9: ["w", "x", "y", "z"]
        }

        if len(digits) == 0:
            return []

        res, sol = [], []
        def backtrack(i):
            if i == len(digits):
                res.append("".join(sol))
                return
            
            for letter in letter_map[int(digits[i])]:
                sol.append(letter)
                backtrack(i + 1)
                sol.pop()
        
        backtrack(0)
        return res
