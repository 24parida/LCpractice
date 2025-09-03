class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        anc_map = [[] for _ in range(n)]
        res = []

        for top, bot in edges:
            anc_map[bot].append(top)

        print(anc_map)
        for i in range(n):
            temp_res = []
            neighbors = anc_map[i][:]
            visited = set()
            while neighbors:                    
                neigh = neighbors.pop()
                if neigh in visited: 
                    continue
            
                neighbors.extend(anc_map[neigh])
                temp_res.append(neigh)
                visited.add(neigh)
            
            temp_res = sorted(temp_res)
            res.append(temp_res)
        
        return res
        
        

