class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 버블 정렬
        iters = len(nums) -1
        for iter in range(iters):
            wall = iters - iter
            for cur in range(wall):
                if nums[cur] > nums[cur+1]:
                    nums[cur], nums[cur+1] = nums[cur+1], nums[cur]
        