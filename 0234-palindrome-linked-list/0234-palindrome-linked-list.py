# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        if not head:
            return True
        
        node = head
        while node is not None:
            lst.append(node.val)
            node = node.next
        
        while len(lst)>1:
            if lst.pop(0) != lst.pop():
                return False
        return True