# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #make a dummy node to avoid with edge case of removing the head node 
        #make the window between slow and fast (n+1) because we want to have slow 
        #right before the nth node 
        dummy = ListNode() 
        dummy.next = head 
        slow = dummy
        fast = dummy 

        for _ in range(n + 1):
            fast = fast.next 
        
        #this while loop leads to slow being at the node before the node we want to remove 
        while fast:
            slow = slow.next 
            fast = fast.next 

        slow.next = slow.next.next 

        return dummy.next 