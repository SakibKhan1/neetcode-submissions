# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        before = dummy #node right before left 
        for _ in range(left - 1):
            before = before.next 

        currRef = before.next #node on left 
        curr = before.next
        prev = None #will hold 3 here in TC1 
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        
        before.next = prev 
        currRef.next = curr 

        return dummy.next
