class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x = x[1:]
            r = -1 * int(x[::-1])
            return r if r >= -2**31 else 0
        else:
            r = int(x[::-1])
            return r if r <= 2**31 else 0