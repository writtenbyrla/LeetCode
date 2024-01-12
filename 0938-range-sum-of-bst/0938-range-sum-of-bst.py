# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
#         low~ high 범위에 있는 수 더하기
        
        # 노드 없으면 0 반환
        if not root:
            return 0

        sum = 0
        stack = [root]

        # dfs 방식(stack 이용)
        while stack:
            node = stack.pop()
            if node:
                # 범위안에 있으면 해당 값 더하고
                if low <= node.val <= high:
                    sum += node.val
                    
                #서브 트리 계속 순회함
                stack.append(node.left)
                stack.append(node.right)

        return sum