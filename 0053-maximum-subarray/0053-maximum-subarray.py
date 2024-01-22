from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = []
        result.append(nums[0])
        for i in range(1, len(nums)):
            # 현재까지의 합과 현재값을 비교해서 더 큰 경우를 result에 담음
            result.append(max(result[i-1] + nums[i], nums[i]))
        return max(result) 