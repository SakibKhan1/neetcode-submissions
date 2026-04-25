class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #so given n which tells us how many open and closed parenthes there should be for end 
        # results, and also that a closed parentheses should be less than open before adding
        # 2 decisions: first is to add an open parentheses as long as it's less than n,
        # and the other decision would be to include a closed parenthese as long as it's less than 
        # n and also less than used open parentheses 

        res = [] 
        curr = []
        def backtrack(openP, closedP, n):
            if openP == n and closedP == n: 
                res.append("".join(curr))
                return 

            if openP < n:
                curr.append("(")
                backtrack(openP + 1, closedP, n)
                curr.pop() 
            if closedP < openP:
                curr.append(")")
                backtrack(openP, closedP + 1, n)
                curr.pop()  
        backtrack(0,0,n)
        return res 
