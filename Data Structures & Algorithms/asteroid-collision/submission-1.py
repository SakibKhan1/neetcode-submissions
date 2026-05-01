class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] 
        for i in range(len(asteroids)):
            boolval = False
            while stack and (
                (asteroids[i] > 0 and stack[-1] < 0) or
                (asteroids[i] < 0 and stack[-1] > 0)
            ):                #so if end of stack is negative and current num is positive, we must:
                # check for value comparison between the 2, if currNum is bigger then we stack.pop()
                # if StackEnd is bigger then we just continue,  
                if abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop() 
                    
                elif abs(stack[-1]) > abs(asteroids[i]):
                    boolval = True  
                    break   
                else: 
                    stack.pop() 
                    boolval = True 
                    break 
            
            if boolval == False:
                stack.append(asteroids[i])
                

        return stack 