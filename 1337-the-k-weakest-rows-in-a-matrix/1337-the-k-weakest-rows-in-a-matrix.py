import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        # 리스트에 1이 나온 개수를 카운트해서 순서대로 담음
        min_heap = [(row.count(1), i) for i, row in enumerate(mat)]
            
        # 리스트 -> 힙
        heapq.heapify(min_heap)
        
        # 답을 반환할 리스트 선언
        answer = []

        for i in range(k):
            count, index = heapq.heappop(min_heap)
            answer.append(index)

        return answer
            
        
        