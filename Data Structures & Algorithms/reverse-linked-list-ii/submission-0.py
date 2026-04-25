# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        
        Lpointer, curr = dummy, head 

        for i in range(left - 1):
            curr = curr.next 
            Lpointer = Lpointer.next 

        prev = None 

        for i in range(right - left + 1):
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 

        Lpointer.next.next = curr
        Lpointer.next = prev  
    
        return dummy.next