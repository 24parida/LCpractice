class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        tokenSet = set(['-', '+', '/', '*'])
        for token in tokens:
            if token in tokenSet:
                a, b = stack.pop(), stack.pop()
                if token == '-':
                    stack.append(b - a)
                elif token == '+':
                    stack.append(b + a)
                elif token == '/':
                    stack.append(int(b / a))
                else:
                    stack.append(b * a)
            else:
                stack.append(int(token))
        
        return stack[-1]