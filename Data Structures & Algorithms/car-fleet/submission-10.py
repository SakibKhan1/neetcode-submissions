class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipfolder = list(zip(position, speed))
        steps = [] 
        zipfolder.sort(reverse=True)

        for p,s in zipfolder:
            steps.append((target - p) / s)

        counter = 1 
        stack = [] 
        for i in steps:
            if stack and stack[-1] < i:
                counter += 1 
            elif stack and stack[-1] > i: 
                stack.pop()
            stack.append(i) 
        return counter 