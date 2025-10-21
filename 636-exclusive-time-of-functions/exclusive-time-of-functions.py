class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n
        curr_proc = []
        prev_time = 0

        for log in logs:
            func, log_type, time = log.split(":")
            func, time = int(func), int(time)
            if log_type == "start":
                if curr_proc:
                    last_func = curr_proc[-1]
                    times[last_func] += time - prev_time
                curr_proc.append(func)
                prev_time = time
            else:
                last_func = curr_proc.pop()
                times[last_func] += time - prev_time + 1
                prev_time = time + 1
            
        
        return times



        