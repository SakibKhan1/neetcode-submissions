class Solution:
    def isValid(self, s: str) -> bool:
        stkMap = {")": "(", "]": "[","}":"{"}
        stack = [] 
        for i in s:
            if i in stkMap:
                if stack and stack[-1] == stkMap[i]:
                    stack.pop()
            stack.append(i)
        return True if stack else False