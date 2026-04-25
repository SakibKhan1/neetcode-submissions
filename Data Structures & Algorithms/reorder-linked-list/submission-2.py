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
        
        #turtle should be at the middle of the list right now 

        #reverse everything from turtle to end of linked list 
        prev = None 

        while turtle: 
            temp = turtle.next 
            turtle.next = prev 
            prev = turtle
            turtle = temp 
        #not turtle will be the reversed second portion of linked list 

        dummy = ListNode() 


        while prev.next:
            temp1 = head.next 
            temp2 = prev.next 
            head.next = prev 
            prev.next = temp1 
            head = temp1 
            prev = temp2 
            
