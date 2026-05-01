class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # take the last 2 things in the stack and 
        # perform whatever operation on them 


        stack = []

        for i in tokens:
            if i == "+":
                pop1 = stack.pop()
                pop2 = stack.pop() 
                stack.append(pop1 + pop2)
            elif i == "-":
                pop1 = stack.pop()
                pop2 = stack.pop() 
                stack.append(pop2 - pop1)
            elif i == "*":
                pop1 = stack.pop()
                pop2 = stack.pop() 
                stack.append(pop1 * pop2)
            elif i == "/":
                pop1 = stack.pop()
                pop2 = stack.pop()
                stack.append(pop2 // pop1)
            else:
                stack.append(int(i))
        return stack[-1]