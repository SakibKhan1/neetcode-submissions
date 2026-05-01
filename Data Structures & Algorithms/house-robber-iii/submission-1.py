# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int: 
        def dfs(root):
            if not root:
                return [0,0]

            
            return [root.val + dfs(root.left)[1] + dfs(root.right)[1], max(dfs(root.left)) + max(dfs(root.right))]

        return max(dfs(root)) 