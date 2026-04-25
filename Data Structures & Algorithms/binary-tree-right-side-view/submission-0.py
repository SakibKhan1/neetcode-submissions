# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = deque([root])

        while q:
            qLen = len(q)
            rightSide = None

            for i in range(qLen):
                node = q.popleft()
                rightSide = node  # all nodes in q are guaranteed to be non-null

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(rightSide.val)

        return res