# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left, right): 
            if not root:
                return True 
            if not (left < root.val < right): 
                return False 
            
            return dfs(root.left, root.val, right) and dfs(root.right, left, root.val) 

        return dfs(root, -1000, 1000)