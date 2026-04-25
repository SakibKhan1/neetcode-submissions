# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = TreeNode() 
        def dfs(root, p, q):
            nonlocal res 
            if not root:
                return 
            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                res = root 
                return 
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
       

        dfs(root,p,q)
        return res 
