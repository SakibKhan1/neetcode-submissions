class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def backtrack(i):
            if i == len(s):
                res.append(curr.copy())
                return

            # try cutting at every possible j position
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    curr.append(substring)
                    backtrack(j)     # explore rest of string

                    curr.pop()         # backtrack

        backtrack(0)
        return res
