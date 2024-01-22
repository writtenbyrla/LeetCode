class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 집이 2개 이하일 경우 큰 수 1개만
        if len(nums)<=2:
            return max(nums)

        dp = [0]*len(nums)
        # 첫번째 집을 시작으로 더 큰 돈을 가진 집으로
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # 이전 이웃집까지의 누적값과 건너 이웃집 누적값+현재집 비교
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1] 