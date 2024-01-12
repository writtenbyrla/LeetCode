# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        # 왼쪽, 오른쪽 서브트리 나누어 dfs 탐색하면서
        # 각각 depth 길이 구하고 더하기
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal result

            # 빈 트리일때 0 반환
            if not node:
                return 0

            # 왼쪽트리, 오른쪽트리 나누어 dfs 탐색
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            #두 길이 합치기
            current_length = left_depth + right_depth

            result = max(result, current_length)

            # 더 깊은 쪽 + 1 =>
            return max(left_depth, right_depth) + 1

        dfs(root)
        return result