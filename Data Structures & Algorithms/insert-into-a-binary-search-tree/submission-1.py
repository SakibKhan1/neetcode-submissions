class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if val < node.val:
                if node.left:
                    dfs(node.left)
                else:
                    node.left = TreeNode(val)
            else:  # val > node.val (guaranteed unique)
                if node.right:
                    dfs(node.right)
                else:
                    node.right = TreeNode(val)


        dfs(root)
        return root
