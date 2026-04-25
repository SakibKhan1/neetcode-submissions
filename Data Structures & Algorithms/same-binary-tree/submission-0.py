# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return []
            left = dfs(root.left)
            right = dfs(root.right)
            children = [] 
            if root.left or root.right:
                children += left if root.left else [None]
                children += right if root.right else [None]
            return [root.val] + children 
        res = False  
        if dfs(p) == dfs(q):
            res = True 
        return res 