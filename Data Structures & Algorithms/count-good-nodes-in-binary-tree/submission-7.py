# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0 
        #we care about side effect here
        def dfs(node, maxVal): 
            nonlocal counter
            if not node:
                return 
            
            if node.val >= maxVal:
                counter += 1 
                maxVal = node.val 
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        dfs(root, float('-inf'))

        return counter 