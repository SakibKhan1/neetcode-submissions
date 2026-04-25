class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        if n == 0: return 2
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack.copy()))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res