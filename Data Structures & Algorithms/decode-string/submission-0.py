class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] 
        res = [] 
        
        for i in range(len(s)):
            if s[i] == "]":
                currword = ""
                number = "" 
                while stack and stack[-1] != "[":
                    currword = stack.pop() + currword
                if stack: 
                    stack.pop() 
                while stack and len(stack[-1]) == 1 and 49 <= ord(stack[-1]) <= 57:
                    number = stack.pop() + number 
                stack.append(currword * int(number))
                currword = ""
                number = ""  
            else:
                stack.append(s[i])

        return "".join(stack)  
