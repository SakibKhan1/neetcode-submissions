class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        curr = []

        def backtrack(i):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return 

            for j in mapping[digits[i]]:
                curr.append(j)
                backtrack(i + 1) 
                curr.pop() 

        backtrack(0)        
        return res 