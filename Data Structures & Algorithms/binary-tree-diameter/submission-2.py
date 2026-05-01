# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 
        def maxDepth(root):
            if not root:
                return 0 

            left = maxDepth(root.left)
            right = maxDepth(root.right)
            return max(left, right) + 1

        def dfs(root):
            nonlocal res 
            if not root:
                return 0 

            left = maxDepth(root.left)
            right = maxDepth(root.right)
            total = left + right 
            res = max(total, res)
        
        dfs(root)
        return res 