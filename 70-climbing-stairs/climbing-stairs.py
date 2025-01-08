class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [1,2]
        if n <= 2:
            return stairs[n-1]
        for i in range(n-2):
            temp = stairs[1]
            stairs[1] = stairs[0] + stairs[1]
            stairs[0] = temp
        
        return stairs[1]
        