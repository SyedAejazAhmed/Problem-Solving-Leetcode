class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**18
        n = len(source)
        nodes = {}
        idx = 0

        def get_id(s):
            nonlocal idx
            if s not in nodes:
                nodes[s] = idx
                idx += 1
            return nodes[s]

        for o, c in zip(original, changed):
            get_id(o)
            get_id(c)

        m = idx
        dist = [[INF]*m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u = nodes[o]
            v = nodes[c]
            dist[u][v] = min(dist[u][v], w)

        for k in range(m):
            for i in range(m):
                if dist[i][k] == INF: 
                    continue
                for j in range(m):
                    if dist[k][j] == INF:
                        continue
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        dp = [INF] * (n + 1)
        dp[n] = 0

        rules_by_len = {}
        for o, c in zip(original, changed):
            l = len(o)
            if l not in rules_by_len:
                rules_by_len[l] = []
            rules_by_len[l].append((o, c))

        for i in range(n-1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i+1]

            for L in rules_by_len:
                if i + L > n:
                    continue
                s_sub = source[i:i+L]
                t_sub = target[i:i+L]

                if s_sub in nodes and t_sub in nodes:
                    u = nodes[s_sub]
                    v = nodes[t_sub]
                    if dist[u][v] != INF:
                        dp[i] = min(dp[i], dist[u][v] + dp[i+L])

        return dp[0] if dp[0] < INF else -1