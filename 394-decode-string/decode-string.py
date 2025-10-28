class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
                continue

            cur = ""
            while stack[-1] != '[':
                cur = stack.pop() + cur
            stack.pop()
            
            cur_num = ""
            while stack and stack[-1].isdigit():
                cur_num = stack.pop() + cur_num
            
            stack.append(int(cur_num) * cur)
        
        return "".join(stack)
