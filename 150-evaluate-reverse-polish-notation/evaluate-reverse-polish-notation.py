class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = set(["+", "-", "*", "/"])
        for i in tokens:
            if i not in operands:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                elif i == "/":
                    stack.append(int(a/b))
        return stack[-1]


        