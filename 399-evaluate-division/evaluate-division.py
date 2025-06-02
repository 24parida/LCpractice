class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj_list = {}
        for i in range(len(equations)):
            l1, l2 = equations[i]
            value = values[i]

            if l1 not in adj_list:
                adj_list[l1] = [(l2, value)]
            else:
                adj_list[l1].append((l2, value))
            
            if l2 not in adj_list:
                adj_list[l2] = [(l1, 1/value)]
            else:
                adj_list[l2].append((l1, 1/value))
        
        res = [-1.0] * len(queries)

        for i in range(len(queries)):
            num, div = queries[i]
            if num not in adj_list:
                continue

            stack = [num]
            visited = set()

            def look_up(running_value, curr_node, look_up_node):
                if curr_node in visited:
                    return 0

                visited.add(curr_node)
                for neigh, val in adj_list[curr_node]:
                    if neigh == look_up_node:
                        return running_value * val
                    temp_res = look_up(running_value * val, neigh, look_up_node)
                    if temp_res != 0:
                        return temp_res
                return 0
            
            temp = look_up(1.0, num, div)
            if temp != 0:
                res[i] = temp
        return res
                    


