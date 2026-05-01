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
                return True 

            if root.left and root.val <= root.left.val:
                return False 
            
            if root.right and root.val >= root.right.val:
                return False 

            left = dfs(root.left)
            right = dfs(root.right)
            if (left and right) == True:
                return True
            else:
                return False 
        return dfs(root)
