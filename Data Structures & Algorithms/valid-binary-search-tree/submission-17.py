# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minval, maxval): 
            if not root: 
                return True 
            if root.val < minval or root.val > maxval: 
                return False 


            left = dfs(root.left, minval, root.val)
            right = dfs(root.right, root.val, maxval)


            if left and right == True:
                return True 
            else:
                return False 

        if dfs(root,float('-inf'), float('inf')) == False:
            return False
        else:
            return True 
