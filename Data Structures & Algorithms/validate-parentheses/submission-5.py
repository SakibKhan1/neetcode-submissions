class Solution:
    def isValid(self, s: str) -> bool:
        stkMap = {")": "(", "]": "[","}":"{"}
        stack = [] 
        for i in s:
            if i in stkMap and stack and stkMap[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return True if stack else False