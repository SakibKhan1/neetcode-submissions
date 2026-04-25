# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        if not root:
            return []
        answer = [] 
        while queue:
            res = [] 
            for _ in range(len(queue)):
                node = queue.popleft() 

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right) 
                res.append(node.val)
            answer.append(res)

        return answer 