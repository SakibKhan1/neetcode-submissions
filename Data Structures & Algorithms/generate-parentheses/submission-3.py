class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] 
        curr = [] 

        if n == 0:
            return ""

        def dfs(openP, closedP):
            if openP == closedP == n:
                res.append("".join(curr.copy()))
                return 

            if openP < n:
                curr.append("(")
                dfs(openP+1, closedP)
                curr.pop() 

            if closedP < openP:
                curr.append(")") 
                dfs(openP, closedP + 1) 
                curr.pop() 

        dfs(0,0)
        return res 