class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)

        graph = defaultdict(list)
        for a, b, cost in times:
            graph[a].append((b, cost))

        dist = [INF] * (n+1)

        q = []
        dist[k] = 0
        heapq.heappush(q, (0, k))

        while q:
            acc, cur = heapq.heappop(q)
            if dist[cur] < acc:
                continue

            for adj, cost in graph[cur]:
                time = acc + cost
                if time < dist[adj]:
                    dist[adj] = time
                    heapq.heappush(q, (time, adj))

        max_dist = max(dist[1:])
        return max_dist if max_dist < INF else -1