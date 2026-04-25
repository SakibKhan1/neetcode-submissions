# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not q and not p:
                return True 
            if not p or not q:
                return False 
            if p.val != q.val:
                return False 

            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right) 

            if (left and right) == True:
                return True 
            else:
                return False 

        if not subRoot:
            return True 
        if not root:
            return False 
        if dfs(root, subRoot):
            return True 
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot) 
        if (left or right) == True:
            return True
        else: 
            return False 

    