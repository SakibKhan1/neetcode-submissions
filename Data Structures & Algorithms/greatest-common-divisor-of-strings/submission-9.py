class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # establish smaller / bigger once per call
        if len(str1) <= len(str2):
            smaller, bigger = str1, str2
        else:
            smaller, bigger = str2, str1

        # base case: exact match
        if smaller == bigger:
            return smaller

        # if bigger cannot be reduced by smaller, no solution
        if not bigger.startswith(smaller):
            return ""

        # strip one block and recurse
        return self.gcdOfStrings(smaller, bigger[len(smaller):])
