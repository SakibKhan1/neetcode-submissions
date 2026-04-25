# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        prevGroup = dummy 

        while True: 
            kthNode = self.getkth(prevGroup, k)
            if not kthNode:
                break 
            nextGroup = kthNode.next
            prev = kthNode.next 
            curr = prevGroup.next
            while curr != nextGroup:
                temp = curr.next 
                curr.next = prev
                prev = curr
                curr = temp

            temp = prevGroup.next 
            prevGroup.next = kthNode
            prevGroup = temp 
        return dummy.next 


    def getkth(self, curr, k): 
        while curr and k != 0: 
            curr = curr.next 
            k -= 1 
        return curr 


   