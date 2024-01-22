class Solution:
    def climbStairs(self, n: int) -> int:
        
        result = [i for i in range(1, n+1)]

        # n이 2보다 작을 경우
        if n <= 2:
            return n

        for i in range(3, n):
            result[i] = result[i - 2] + result[i - 1]

        return result[n-1]