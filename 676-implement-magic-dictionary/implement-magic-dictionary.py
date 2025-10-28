class MagicDictionary:

    def __init__(self):
        self.dict = collections.defaultdict(int)
        self.a = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            tmp_word = list(word)
            self.a.add(word)
            for i in range(len(word)):
                tmp = tmp_word[i]
                tmp_word[i] = '*'
                self.dict["".join(tmp_word)] += 1
                tmp_word[i] = tmp
                

    def search(self, searchWord: str) -> bool:
        in_dict = searchWord in self.a

        tmp = list(searchWord)
        for i in range(len(searchWord)):
            t = tmp[i]
            tmp[i] = "*"

            b = "".join(tmp)
            if (not in_dict and b in self.dict) or (in_dict and self.dict[b] >= 2):
                return True
            tmp[i] = t
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)