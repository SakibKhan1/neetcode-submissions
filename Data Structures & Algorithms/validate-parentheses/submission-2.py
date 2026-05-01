class Solution:
    def isValid(self, s: str) -> bool:
        stkMap = {")": "(", "]": "[","}":"{"}
        stack = [] 
        for i in s:
            if i in stkMap and stkMap[i] == stack[-1] and stack:
                stack.pop()
            stack.append(i)
        return True if stack else False