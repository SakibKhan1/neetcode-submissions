class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, openN, closeN):
            # base case: if both open and close reach n, we have a valid combo
            if openN == closeN == n:
                res.append(curr)
                return

            # add an opening parenthesis if we still can
            if openN < n:
                backtrack(curr + "(", openN + 1, closeN)

            # add a closing parenthesis if it doesn’t exceed open count
            if closeN < openN:
                backtrack(curr + ")", openN, closeN + 1)

        backtrack("", 0, 0)
        return res
