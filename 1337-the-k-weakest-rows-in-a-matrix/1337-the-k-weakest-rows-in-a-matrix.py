import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        min_heap = []
        
        for i in range(len(mat)):
            cnt = collections.Counter(mat[i])
            heapq.heappush(min_heap, (cnt[1], i))
        
        answer = []

        for i in range(k):
            answer.append(heapq.heappop(min_heap)[1])

        return answer
