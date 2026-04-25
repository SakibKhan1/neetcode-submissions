# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #we want to use the floyd's algo to find the middle of the list 
        #and then we reverse the second half of the list
        #we then take the two lists and then merge them together using alternate nodes
        #from the first and second halves 
        if not head or not head.next:
            return 
        #part 1: finding middle of list using floyd's algo 
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        #part 2: reversing second half of the list and cutting off second half from first half
        curr = slow.next
        slow.next = None 
        prev = None 
        while curr: 
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 

        #part 3: merging both lists into one 
        first, second = head, prev 

        while second: 
            temp1 = first.next
            temp2 = second.next 
            first.next = second 
            second.next = temp1 
            first = temp1 
            second = temp2  













        