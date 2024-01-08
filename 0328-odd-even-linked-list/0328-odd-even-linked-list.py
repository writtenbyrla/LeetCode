# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        odd = head #홀수
        even = head.next #짝수
        even_head = head.next 
        
        while even and even.next: 
            odd.next, even.next = odd.next.next, even.next.next # 1개 건너뛴 노드를 참조하도록 함
            odd, even = odd.next, even.next # 다음 노드로 이동하면서 odd에 홀수끼리 연결, even에 짝수끼리 연결
        
        odd.next = even_head # 홀수 마지막 노드에 짝수 첫 노드 연결
        return head