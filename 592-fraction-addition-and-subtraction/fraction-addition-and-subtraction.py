class Solution:
    def fractionAddition(self, expression: str) -> str:
        sign = 1
        n, d = 0, 1
    
        i = 0

        while i < len(expression):
            pn, pd = 0, 0
            
            if not expression[i].isdigit():
                if expression[i] == '-':
                    sign = -1
                elif expression[i] == '+':
                    sign = 1
                i += 1
            
            while i < len(expression) and expression[i].isdigit():
                pn = 10 * pn + int(expression[i])
                i += 1
            i += 1
            
            while i < len(expression) and expression[i].isdigit():
                pd = 10 * pd + int(expression[i])
                i += 1
            
            pn *= sign
            n = n * pd + pn * d
            d = pd * d
        
        
        def gcd(a, b):
            if a == 0:
                return b
            
            return gcd(b % a, a)
        
        gcd = abs(gcd(n, d))
        n //= gcd
        d //= gcd
        return f"{n}/{d}"



            

                


            