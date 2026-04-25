# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        while curr.next: 
            a = curr
            b = curr.next 

            res = -1 
            for i in range(1, min(a.val,b.val) + 1):
                if a.val % i == 0 and b.val % i == 0:
                    res = i 

            a.next = ListNode(res) 
            a.next.next = b 
            curr = b 
        return head 
             