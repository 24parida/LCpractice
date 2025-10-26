class Node:
    def __init__(self, char):
        self.c = {}
        self.ch = char
        self.end = False
        self.word = None

    def addWord(self, word):
        curr = self
        for w in word:
            if w not in curr.c:
                curr.c[w] = Node(w)
            curr = curr.c[w]
        
        curr.end = True
        curr.word = word
            



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node("")

        for i in words:
            root.addWord(i)
        
        visited = set()
        res = set()
        def dfs(x, y, node):
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                return
            if (x,y) in visited or board[x][y] not in node.c:
                return
            
            visited.add((x,y))

            node = node.c[board[x][y]]
            if node.end: res.add(node.word)

            dfs(x+1, y, node)
            dfs(x-1, y, node)
            dfs(x, y+1, node)
            dfs(x, y-1, node)

            visited.remove((x,y))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,root)
        
        return list(res)
            