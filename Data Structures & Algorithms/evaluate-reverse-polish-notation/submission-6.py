class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = [] 
        for i in tokens:
            if i == "+":
                stk.append(stk.pop() + stk.pop())
            elif i == "-":
                a = stk.pop()
                b = stk.pop()  
                stk.append(b - a)
            elif i == "*":
                stk.append(stk.pop() * stk.pop())
            elif i == "/":
                a = stk.pop()
                b = stk.pop() 
                stk.append(int(b / a))
            else:
                stk.append(int(i)) 
            
        return stk[0]