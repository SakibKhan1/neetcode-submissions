class Solution:
    def isValid(self, s: str) -> bool:
        # s="[(])" failing 
        mapping = {")": "(", "]": "[","}":"{"}
        stack = [] 
        for i in s:
            if i in mapping.keys():
                if stack and mapping[i] == stack[-1]:
                    stack.pop() 
            if i not in mapping:
                stack.append(i)

            if stack:
                return True
            else:
                return False 
                
            