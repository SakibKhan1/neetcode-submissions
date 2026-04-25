# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #we can reverse the entire linked list 
        #create a remove function that removes at a certain index 

         
        dummy = ListNode() 
        dummy.next = head 
        slow = dummy
        fast = dummy 
        for _ in range(n + 1):
            fast = fast.next 

        
        while fast: 
            slow = slow.next
            fast = fast.next 

        slow.next = slow.next.next

        return dummy.next