class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tmap = collections.defaultdict(list)
        N = len(transactions)
        res = [False] * N

        for i in range(N):
            tr = transactions[i]
            n, t, a, c = tr.split(",")
            t, a = int(t), int(a)

            if a > 1000: res[i] = True
            tmap[n].append((n,t,a,c,i))
        
        for name in tmap:
            for i in range(len(tmap[name])):
                for j in range(i + 1, len(tmap[name])):
                    if abs(tmap[name][i][1] - tmap[name][j][1]) <= 60 and tmap[name][i][3] != tmap[name][j][3]:
                        res[tmap[name][i][-1]] = True
                        res[tmap[name][j][-1]] = True
        
        return [transactions[i] for i in range(len(transactions)) if res[i]]




        

