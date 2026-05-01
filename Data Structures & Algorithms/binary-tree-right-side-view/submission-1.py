# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)          # add current node first
            if node.right:
                dfs(node.right)           # go as far right as possible
            elif node.left:               # if no right child, go left once
                dfs(node.left)            # include fallback left edge

        dfs(root)
        return res
            