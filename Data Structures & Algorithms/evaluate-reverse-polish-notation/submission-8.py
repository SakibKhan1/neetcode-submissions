class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # take the last 2 things in the stack and 
        # perform whatever operation on them 


        stack = []

        for i in tokens:
            if i == "+":
                total = int(stack[-1]) + int(stack[-2])
                stack.append(total)
            elif i == "-":
                total = int(stack[-2]) - int(stack[-1])
                stack.append(total)
            elif i == "*":
                total = int(stack[-2]) * int(stack[-1])
                stack.append(total)
            elif i == "/":
                total = int(stack[-2]) // int(stack[-1])
                stack.append(total) 
            else:
                stack.append(i)
        return stack[-1]