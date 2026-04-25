# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        turtle = head 
        hare = head 

        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next 

        #turtle should be at the middle of the linked list 

        curr = turtle.next 
        turtle.next = None 
        prev = None 
        
        
        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 

        #we reversed the linked list starting from turtle to end of linked list 
        #prev variable holds the head of the reversed 2nd half of the input list 

   
        curr = head 
        while prev:
            temp1 = curr.next 
            temp2 = prev.next 
            curr.next = prev 
            prev.next = temp1

            curr = temp1 
            prev = temp2 

        



