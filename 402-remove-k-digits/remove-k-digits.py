class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and stack[-1] > c and k > 0:
                stack.pop()
                k -= 1
            stack.append(c)
        

        res = "".join(stack[:len(stack)-k])
        res = res.lstrip("0")
        return res if res else "0"