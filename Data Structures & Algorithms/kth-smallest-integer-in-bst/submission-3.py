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
        minHeap = [] 
        queue = deque([root])
        while queue:
            node = queue.popleft() 
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            minHeap.append(node.val) 
        heapq.heapify(minHeap)
        i = 0 
        res = 0 
        while i < k: 
            res = heapq.heappop(minHeap)
            i += 1 
        return res
        