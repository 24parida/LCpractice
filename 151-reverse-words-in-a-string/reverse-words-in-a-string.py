class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = words[::-1]
        words = [i for i in words if i != '']

        return " ".join(words)