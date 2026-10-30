import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        pq = [(0, 0, 1)]
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            if d > dist[u][count]:
                continue

            if u == n - 1:
                return d
                
            for v, w in adj[u]:
                nxt_count = count + 1 if labels[u] == labels[v] else 1

                if nxt_count <= k:
                    nxt_d = d + w
                    if nxt_d < dist[v][nxt_count]:
                        dist[v][nxt_count] = nxt_d
                        heapq.heappush(pq, (nxt_d, v, nxt_count))
                        
        return -1
