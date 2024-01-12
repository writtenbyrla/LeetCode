# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        # low~ high 범위에 있는 수 더하기
        
        # 노드 없으면 0 반환
        if not root:
            return 0

        sum = 0
        stack = [root]

        # 1. dfs 방식(stack 이용) - 트리
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         # 범위안에 있으면 해당 값 더하고
        #         if low <= node.val <= high:
        #             sum += node.val
        #
        #         # 서브 트리 계속 순회함
        #         stack.append(node.left)
        #         stack.append(node.right)

        #bst = 완전 이진 트리이므로 서브트리의 왼쪽은 값이 작고 오른쪽은 값이 크다
        # 2. 현재 노드 크기를 low, high 비교해서 오른쪽으로 갈지 왼쪽으로 갈지 결정
        
        while stack:
            node = stack.pop()
            if node:
                if node.val < low:
                    stack.append(node.right)
                if node.val > high:
                    stack.append(node.left)
                if low <= node.val <= high:
                    sum += node.val
                    stack.append(node.left)
                    stack.append(node.right)

        return sum