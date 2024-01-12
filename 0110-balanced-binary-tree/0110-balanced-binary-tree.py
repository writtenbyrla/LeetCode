# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 서브트리의 깊이 차이가 나지 않아야 true
        # dfs 방식으로 재귀호출하여 서브트리의 depth 비교
        
        result = True
        
        def dfs(node):
            nonlocal result
            
            # 종료 조건
            if not node:
                return 0
            
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            # 서브트리 높이 차이가 1보다 크면 False
            if abs(left_len - right_len) > 1:
                result = False
            
            # 1씩 증가시켜 깊이 증가
            return max(left_len, right_len)+1  
            
        dfs(root)    
        return result