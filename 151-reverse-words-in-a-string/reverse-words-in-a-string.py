class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = words[::-1]
        print(words)
        res = ""
        for word in words:
            if word == "":
                continue
            res += word + " "

        return res[:-1]