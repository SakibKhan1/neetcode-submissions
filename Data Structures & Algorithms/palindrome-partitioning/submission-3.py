class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = [] 
        curr = [] 

        def backtrack(i):
            if i == len(s):
                res.append(curr.copy())

            for j in range(i, len(s)):
                subString = s[i : j + 1] 
                if subString == subString[::-1]:
                    curr.append(subString)
                    backtrack(j + 1) 
                    curr.pop() 

        backtrack(0) 
        return res 