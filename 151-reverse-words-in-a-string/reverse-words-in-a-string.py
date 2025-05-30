class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.split(" ")
        # words = words[::-1]
        # print(words)
        # res = ""
        # for word in words:
        #     if word == "":
        #         continue
        #     res += word + " "

        # return res[:-1]

        builder = collections.deque()

        start = -1
        i = 0

        while i < len(s):
            if s[i] != " ":
                start = i
                while i < len(s) and s[i] != " ":
                    i += 1
                builder.appendleft(s[start:i])
            i += 1
        return " ".join(builder)
            