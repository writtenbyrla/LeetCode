class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(start, end):
            if start > end:
                return -1

            mid = (start+end)//2

            if nums[mid] < target:
                return bs(mid+1, end)
            elif nums[mid] > target:
                return bs(start, mid-1)
            else:
                return mid
            
        return bs(0, len(nums)-1)
            