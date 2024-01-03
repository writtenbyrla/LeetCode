class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        #i,j,k 세 수의 합
        for i in range(len(nums)-2):
            
            # 중복값 건너뛰기
            if i>0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum<0: #합이 0보다 작으면 값이 더 커야하므로 오른쪽으로 이동
                    left+=1
                elif sum>0: #합이 0보다 크면 값이 더 작아야 하므로 왼쪽으로 이동    
                    right-=1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                     
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left<right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    # while문이 false일 경우 포인터 이동
                    left += 1
                    right -= 1

        return results
            
