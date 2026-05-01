class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        nodes = []

        # collect all nodes with parent references
        def dfs(node, parent):
            if not node:
                return
            nodes.append((node, parent))
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # sort by value descending (greedy)
        nodes.sort(key=lambda x: x[0].val, reverse=True)

        blocked = set()
        total = 0

        for node, parent in nodes:
            if node in blocked:
                continue

            # choose node
            total += node.val

            # block all directly connected nodes
            blocked.add(node)
            if parent:
                blocked.add(parent)
            if node.left:
                blocked.add(node.left)
            if node.right:
                blocked.add(node.right)

        return total
