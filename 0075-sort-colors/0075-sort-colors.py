class Solution:
    def sortColors(self, nums: List[int]) -> None:

        
        # 선택 정렬(최솟값을 기준으로 정렬)
        # 가장 작은 수를 제일 앞으로 보내면서 정렬
        for i in range(len(nums)-1):
            minn = i
            for cur in range(i+1, len(nums)): # 맨 앞에 간 최솟값 제외 다음 자리부터 비교
                if nums[cur] < nums[minn]: # 최솟값 자리에 더 큰 수가 있는 경우
                    minn = cur #현재 비교중인 값의 인덱스를 최솟값으로 설정
                    
            if minn != i: # 최솟값을 찾으면 자리 바꾸기
                nums[i], nums[minn] = nums[minn], nums[i]
                