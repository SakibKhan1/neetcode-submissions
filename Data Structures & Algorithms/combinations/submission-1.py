class Solution:
    def combine(self, n: int, k: int):
        res = []
        curr = []

        def backtrack(start):
            # base case: we have k numbers
            if len(curr) == k:
                res.append(curr.copy())
                return

            # choose the next number
            for num in range(start, n + 1):
                curr.append(num)
                backtrack(num + 1)   # move forward only
                curr.pop()           # undo choice

        backtrack(1)
        return res
