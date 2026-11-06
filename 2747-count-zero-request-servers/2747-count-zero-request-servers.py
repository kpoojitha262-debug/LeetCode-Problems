class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        res = [0] * len(queries)
        server_count = {}
        
        left = 0
        right = 0
        m = len(logs)
        
        for q, orig_idx in sorted_queries:
            window_start = q - x
            window_end = q
            
            while right < m and logs[right][1] <= window_end:
                server_id = logs[right][0]
                server_count[server_id] = server_count.get(server_id, 0) + 1
                right += 1
                
            while left < m and logs[left][1] < window_start:
                server_id = logs[left][0]
                server_count[server_id] -= 1
                if server_count[server_id] == 0:
                    del server_count[server_id]
                left += 1
                
            res[orig_idx] = n - len(server_count)
            
        return res