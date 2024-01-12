# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        # 조건1) 현재 노드 == val일때
        # 조건2) node.left < node.val < node.right인 경우
        # node, node.left, node.right를 result에 추가

        stack = [root]

        while stack:
            node = stack.pop()
            if node is None:
                continue
                

            if node.val == val:
                return node 
            elif node.val > val:
                stack.append(node.left)
            else:
                stack.append(node.right)


        return None