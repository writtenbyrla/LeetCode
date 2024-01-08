# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 정렬된 연결 리스트 2개를 오름차순으로 병합하여 하나의 연결리스트로 만드는 문제
        # list1 기준으로 정렬하여 반환
        # 1. 오름차순 정렬: 리스트의 노드 끼리 값을 비교하여 더 작은 수가 list1에 오도록 배치
        # 2. 병합: list1의 마지막 노드가 list2 첫 노드를 참조하게 하여 병합        
        
        # list1이 비어있는 경우 => list2의 값을 list1로 보내야 함 
        # list2의 값이 더 작은 경우 오름차순 정렬을 위하여 list1의 값과 바꾸어줌
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        
        # mergeTwoList를 이용하여 list1의 마지막 노드가 list2의 첫 노드를 참조하게 함으로써 사실상 병합이 됨
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
            
        return list1
            