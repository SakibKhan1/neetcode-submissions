# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root
        def dfs(root,p,q):
            nonlocal res 
            if not root:
                return 

            dfs(root.left,p,q)
            dfs(root.right,p,q)
            if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
                # This means the current node is between p and q — potential LCA
                res = root
                return 

        dfs(root,p,q)
        return res 
            