from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0 
        queue = deque([[root, -10000]])

        while queue:
            node, maxsofar = queue.popleft() 
            if node.val >= maxsofar:
                res += 1 
                maxsofar = node.val 

            if node.left:
                queue.append([node.left, max(maxsofar, node.val)])
            if node.right:
                queue.append([node.right, max(maxsofar, node.val)])
        return res 