import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n, m = len(servers), len(tasks)
        
        available = [(servers[i], i) for i in range(n)]
        heapq.heapify(available)
        
        busy = []
        ans = [0] * m
        curr_time = 0
        
        for j in range(m):
            curr_time = max(curr_time, j)
            
            while busy and busy[0][0] <= curr_time:
                _, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))
                
            if not available:
                curr_time = busy[0][0]
                while busy and busy[0][0] <= curr_time:
                    _, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))
            
            weight, idx = heapq.heappop(available)
            ans[j] = idx
            heapq.heappush(busy, (curr_time + tasks[j], weight, idx))
            
        return ans