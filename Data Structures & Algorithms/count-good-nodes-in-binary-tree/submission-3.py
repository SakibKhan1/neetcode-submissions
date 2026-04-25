# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        
        def dfs(node, parent):
            nonlocal good
            
            if not node: return 0
            
            if node.val >= parent:
                good += 1
            
            maxSoFar = max(parent, node.val)
            dfs(node.left, maxSoFar)
            dfs(node.right, maxSoFar)
    
        dfs(root, root.val)
        return good