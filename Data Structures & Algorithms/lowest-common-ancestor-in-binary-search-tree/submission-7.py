class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST property lets us guide the search efficiently
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left  # both are smaller → go left
            elif p.val > root.val and q.val > root.val:
                root = root.right  # both are larger → go right
            else:
                return root  # this is the split point (LCA)
