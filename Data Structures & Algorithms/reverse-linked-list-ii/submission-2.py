# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        prev = dummy #node right before left 
        for _ in range(left - 1):
            prev = prev.next 

        currRef = prev.next #node on left 
        curr = prev.next
        prev = None #will hold 3 here in TC1 
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        
        currRef.next = curr 
        dummy.next = prev

        return dummy.next
