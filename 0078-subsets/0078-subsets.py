class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []

        # 시작 지점, 현재 문자 조합
        def dfs(start, current):
            
            # 모든 조합을 넣기 위해 따로 조건없이 answer에 바로 추가
            # current가 바뀌면 변경된 값으로 저장되기 때문에 복사본으로 추가
            answer.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                dfs(i+1, current)
                current.pop()

        dfs(0, [])
        
        return answer
            
        