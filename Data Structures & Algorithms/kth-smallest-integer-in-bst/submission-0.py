from collections import deque
import heapq 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        res = [] 
        while queue:   
            node = queue.popleft() 
            res.append(node.val) 

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        heapq.heapify(res) 
        res2 = [] 
        i = 0  
        while i < k: 
            res2.append(heapq.heappop(res)) 
            i += 1 

        return res2[-1]

