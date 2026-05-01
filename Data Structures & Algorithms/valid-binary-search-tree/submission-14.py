class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfsLeft(node, maxVal):
            if not node:
                return True
            if node.val >= maxVal:
                return False
            return dfsLeft(node.left, maxVal) and dfsLeft(node.right, maxVal)

        def dfsRight(node, minVal):
            if not node:
                return True
            if node.val <= minVal:
                return False
            return dfsRight(node.left, minVal) and dfsRight(node.right, minVal)

        # Check current node
        left_valid = dfsLeft(root.left, root.val)
        right_valid = dfsRight(root.right, root.val)

        # Recursively ensure subtrees are valid too
        return left_valid and right_valid 


