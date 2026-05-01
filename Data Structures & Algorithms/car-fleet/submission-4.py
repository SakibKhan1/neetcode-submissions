import math 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #use math.ceil for decimal values 
        steps = [] 
        stack = [] 
        counter = 0
        for i in range(len(position)):
            calc = math.ceil((target - position[i]) / speed[i])
            steps.append(calc)

        for i in range(len(steps)):
            while stack and steps[i] > stack[-1]:
                stack.pop() 
                counter += 1
            stack.append(steps[i])
       
        return counter + len(stack) - 1
        # [1 steps, 2 steps,  3 steps]   the 1 will combine with 3 and the 3 will never combine w 2
        # if a smaller number appears before a bigger number, combine immediately