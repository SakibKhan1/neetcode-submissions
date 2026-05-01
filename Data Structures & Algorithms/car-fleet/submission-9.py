class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipfolder = list(zip(position, speed))
        steps = [] 
        zipfolder.sort(reverse=True)

        for p,s in zipfolder:
            steps.append((target - p) / s)

        stack = [] 
        for i in steps:
            while stack and stack[-1] > i:
                stack.pop() 
            stack.append(i) 
        return len(stack) - 1