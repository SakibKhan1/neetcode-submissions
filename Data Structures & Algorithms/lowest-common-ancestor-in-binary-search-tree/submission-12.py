class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return None

            # If both p and q are smaller → go left
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)

            # If both p and q are larger → go right
            if p.val > node.val and q.val > node.val:
                return dfs(node.right)

            # Otherwise, this node is the split point → LCA
            return node

        return dfs(root)
