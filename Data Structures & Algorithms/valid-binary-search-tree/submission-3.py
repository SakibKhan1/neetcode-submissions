# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root): 
            if not root: 
                return False 

            if (root.left and root.left.val > root.val):
                return False
            if (root.right and root.right.val < root.val):
                return False 

            dfs(root.left)
            dfs(root.right) 
            return True 

        if dfs(root):
            return True
        else:
            return False 