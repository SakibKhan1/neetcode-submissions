class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] 
        for i in range(len(asteroids)):
            boolval = False
            while stack and ((asteroids[i] < 0 and stack[-1] > 0)):          
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