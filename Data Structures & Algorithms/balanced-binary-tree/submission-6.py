# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        boolval = True 
        def dfs(root):
            nonlocal boolval
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right) 
            if abs(left - right) > 1: 
                boolval = False 
            return max(left, right) + 1 

        dfs(root)
        if boolval == True:
            return True
        else:
            return False 