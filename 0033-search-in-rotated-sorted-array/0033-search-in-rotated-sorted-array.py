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
        
        # 최솟값 찾기(left)
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # 중간지점의 값이 더 크면
                left = mid + 1  # 오른쪽으로 더 이동해서 찾아야함
            else:
                right = mid # 중간지점의 값이 더 작으면 왼쪽으로 이동해서 찾아야함
        
        added = nums + nums[:left] # 최솟값 기준으로 뒤에 덧붙임
        result = bs(added, left, len(added)-1)
        
        if result == -1:
            return result
        else:
            return result % len(nums) # 원래 인덱스 찾아주기