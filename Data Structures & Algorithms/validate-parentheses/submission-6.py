class Solution:
    def isValid(self, s: str) -> bool:
        # we want to only compare to stack[-1] given 
        # it's in the mapping and i == closing
        mapping = {")": "(", "]": "[","}":"{"}
        stack = [] 
        for i in s:
            if i in mapping:
                if stack and mapping[i] == stack[-1]:
                    stack.pop() 
            if i not in mapping:
                stack.append(i)

            if stack:
                return True
            else:
                return False 
                
            