# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Calculate the integer values of the two linked lists
        curr = l1
        result = 0
        multiplier = 1
        while curr:
            result += curr.val * multiplier
            multiplier *= 10
            curr = curr.next
        
        curr2 = l2
        result2 = 0
        multiplier2 = 1
        while curr2:
            result2 += curr2.val * multiplier2
            multiplier2 *= 10
            curr2 = curr2.next
        
        # Step 2: Calculate the total sum of both values
        total = result + result2
        
        # Step 3: Convert the total sum into a reversed linked list
        if total == 0:
            return ListNode(0)
        
        new_head = ListNode(total % 10)
        total //= 10
        curr = new_head
        
        while total > 0:
            curr.next = ListNode(total % 10)
            total //= 10
            curr = curr.next
        
        return new_head