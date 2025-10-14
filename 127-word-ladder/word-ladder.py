class Solution:
    def oneLetterDiff(self, i: str, j: str) -> bool:
        if len(i) != len(j): 
            return False
        diffs = 0
        for a, b in zip(i, j):
            if a != b:
                diffs += 1
                if diffs > 1:
                    return False
        return diffs <= 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = collections.defaultdict(list)
        wordList.append(beginWord)
        for i in wordList:
            temp_i = []
            for j in adj_list:
                if self.oneLetterDiff(i, j):
                    adj_list[j].append(i)
                    temp_i.append(j)
            adj_list[i] = temp_i
        print(adj_list)
        
        q = collections.deque([(1, beginWord)])
        visited = set([beginWord])
        while q:
            dist, word = q.popleft()
            if word == endWord:
                return dist
            else:
                for neigh in adj_list[word]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append((dist + 1, neigh))
        
        return 0