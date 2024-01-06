import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # 최소힙으로 변환되는 것이 기본이므로 최대힙으로 heapify를 해야함
        # 최대힙을 저장할 공간을 만들고, nums의 요소를 음수로 저장하면 최소힙과 반대로 저장되므로 최대힙이 됨
        
        max_heap = []
        
        for item in nums:
            heapq.heappush(max_heap, -item)
        
        num1 = -heapq.heappop(max_heap)
        num2 = -heapq.heappop(max_heap)
        
        return (num1-1)*(num2-1)
        
        