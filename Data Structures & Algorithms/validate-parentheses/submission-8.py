class Solution:
    def isValid(self, s: str) -> bool:
        # s="[(])" failing 
        mapping = {")": "(", "]": "[","}":"{"}
        stack = [] 
        for i in s:
            if i in mapping:
                if stack and mapping[i] == stack[-1]:
                    stack.pop() 
            if i not in mapping:
                stack.append(i)

        if not stack:
            return True 
        else:
            return False 
                
            