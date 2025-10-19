class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res, sol = [], []
        
        def backtrack(i, cur, prev):
            if i >= len(num):
                if cur == target:
                    res.append("".join(sol))
                return

            range_to_check = range(i, len(num)) if num[i] != '0' else range(i, i+1)
            for j in range_to_check:
                parsed_num = int(num[i:j+1])

                if i == 0:
                    sol.append(str(parsed_num))
                    backtrack(j+1, parsed_num, parsed_num)
                    sol.pop()
                    continue

                # try add
                sol.append(f"+{parsed_num}")
                backtrack(j+1, cur + parsed_num, parsed_num)
                sol.pop()

                # try sub
                sol.append(f"-{parsed_num}")
                backtrack(j+1, cur - parsed_num, -parsed_num)
                sol.pop()

                # try mult
                sol.append(f"*{parsed_num}")
                new_num = (cur - prev) + (prev * parsed_num)
                new_prev = prev * parsed_num
                backtrack(j+1, new_num, new_prev)
                sol.pop()

        backtrack(0, 0, 0)
        return res