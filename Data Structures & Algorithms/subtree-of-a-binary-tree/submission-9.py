# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sametree(root,root2):
            if not root and not root2:
                return True 
            if not root or not root2 or root.val != root2.val:
                return False 

            left = sametree(root.left, root2.left)
            right = sametree(root.right, root2.right) 
            if (left and right) == True:
                return True 
        boolval = False 
        def dfs(root, subRoot):
            nonlocal boolval 
            if not root:
                return True
            if sametree(root,subRoot) == True:
                boolval = True 
                return 

            left = dfs(root.left, subRoot)
            right = dfs(root.right, subRoot) 
        dfs(root, subRoot)
        return boolval