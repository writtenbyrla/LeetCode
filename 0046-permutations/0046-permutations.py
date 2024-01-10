class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        visited = [0]*len(nums)
        
        def dfs(start, visited, current):
            
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for i in range(len(nums)):
                
                if not visited[i]:
                    visited[i] = 1
                    current.append(nums[i])
                    
                    dfs(start+1, visited, current)
                    
                    current.pop()
                    visited[i] = 0
        
        dfs(1, visited, [])
            
        return result