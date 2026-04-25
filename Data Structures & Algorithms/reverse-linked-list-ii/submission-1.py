# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 

        curr = dummy 
        
        for _ in range(left - 1):
            curr = curr.next 

        prev = None 
        curr2ref = curr.next 
        curr2 = curr.next 
        for _ in range(right - left + 1):
            temp = curr2.next 
            curr2.next = prev 
            prev = curr2
            curr2 = temp 
        
        curr.next = prev 
        curr2ref.next = curr2

        return dummy.next 
