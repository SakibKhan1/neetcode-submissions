from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1 
        maxsofar = root.val 
        queue = deque([root])

        while queue:
            node = queue.popleft() 
            if node.right and node.right.val >= maxsofar:
                res += 1 
                queue.append(node.right)
            if node.left and node.left.val >= maxsofar:
                res += 1 
                queue.append(node.left) 
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res 

