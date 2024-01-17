class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # points: 좌표 리스트 , # (0,0)과 가까운 좌표 k개 출력
        
        heap = []
        for (x, y) in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))
            
        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
            
        return result