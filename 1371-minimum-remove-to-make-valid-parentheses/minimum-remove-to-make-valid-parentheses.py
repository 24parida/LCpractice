class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        diff = 0
        for c in s:
            if c == '(':
                diff += 1
                res.append(c)
            elif c == ')' and diff > 0:
                diff -= 1
                res.append(c)
            elif c.isalpha():
                res.append(c)

        res = res[::-1]
        new = []
        for c in res:
            if c == '(' and diff > 0:
                diff -= 1
            else:
                new.append(c)
        
        return "".join(new[::-1])


