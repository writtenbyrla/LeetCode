class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(added, start, end):
            if start > end:
                return -1
            
            mid = (start+end) // 2
            
            if added[mid] < target:
                return bs(added, mid+1, end)
            elif added[mid] > target:
                return bs(added, start, mid-1)
            else:
                return mid
        
        if not nums:
            return -1  
        
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        added = nums + nums[:left]
        result = bs(added, left, len(added)-1)
        
        if result == -1:
            return result
        else:
            return result % len(nums)