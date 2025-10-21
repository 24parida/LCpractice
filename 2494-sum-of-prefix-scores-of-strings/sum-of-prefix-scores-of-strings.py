class node:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = node()

    def addWord(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = node()
            curr = curr.children[w]
            curr.count += 1
    
    def count(self, word):
        res = 0
        curr = self.root
        for w in word:
            if w not in curr.children:
                return res
            curr = curr.children[w]
            res += curr.count
        
        return res
        


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t = Trie()
        res = []
        for word in words:
            t.addWord(word)
        
        for word in words:
            res.append(t.count(word))
        
        return res

        
        