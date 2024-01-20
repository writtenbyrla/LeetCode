class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 가장 싼 가격
        # src 출발지, dst 도착지, k 경유 횟수
        graph = defaultdict(list) # 비용
        visited = [0] * n # 경유 횟수
        for departure, arrival, price in flights:
            graph[departure].append((arrival, price))

        q = []
        heapq.heappush(q, (0, 0, src))

        while q:
            acc, count, cur = heapq.heappop(q)
            if cur == dst:
                return acc
            if visited[cur]==0 or visited[cur]  > count:
                visited[cur] = count

                for adj, cost in graph[cur]:
                    if count <= k:
                        price_sum = acc + cost
                        heapq.heappush(q, (price_sum, count+1, adj))
        return -1