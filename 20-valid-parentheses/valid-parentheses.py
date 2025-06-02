class Solution:
    def isValid(self, s: str) -> bool:
        reverse_map = {")": "(", "]":"[", "}":"{"}
        stack = []
        for i in s:
            if i not in reverse_map:
                stack.append(i)
            else:
                if len(stack) == 0 or stack[-1] != reverse_map[i]:
                    return False
                stack.pop()
            
        return len(stack) == 0
        