import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue

            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return dist[n-1] if dist[n-1] < INF else -1
