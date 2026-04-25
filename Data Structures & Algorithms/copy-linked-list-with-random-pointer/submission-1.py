"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        LLdict = {None: None} 
        while curr: 
            LLdict[curr] = Node(curr.val)
            curr = curr.next 

        curr = head 
        while curr: 
            copy = LLdict[curr]
            copy.next = LLdict[curr.next]
            copy.random = LLdict[curr.random]
            curr = curr.next 

        return LLdict[head]