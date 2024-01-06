import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # 최소힙으로 변환되는 것이 기본이므로 최대힙으로 heapify를 해야함
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        num1 = -heapq.heappop(nums)
        num2 = -heapq.heappop(nums)
        
        return (num1-1)*(num2-1)
        