class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #backtrack solution 

        res = [] 
        def dfs(openN, closedN, curr):
            
            if openN == closedN == n:
                res.append(curr) 
                return 

            if openN < n: 
                
                dfs(openN + 1, closedN, curr + "(")

            if closedN < openN:
             
                dfs(openN, closedN + 1, curr + ")")

        dfs(0,0, "")
        return res 