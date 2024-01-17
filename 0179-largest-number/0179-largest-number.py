from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # nums를 정렬해서 가장 큰 수 만들기
        # 버블정렬 이용하여 앞뒤로 붙은 두개씩 x+y, y+x 중 더 큰 수가 앞으로 오도록 정렬

        # 문자열로 변환
        nums = [str(num) for num in nums]

        length = len(nums) -1 # 반복 횟수
        for cur_idx in range(length):
            wall = length - cur_idx

            for cur in range(wall):
                if nums[cur] + nums[cur+1] < nums[cur+1] + nums[cur]:
                    nums[cur], nums[cur+1] = nums[cur+1], nums[cur]
        return str(int(''.join(nums)))