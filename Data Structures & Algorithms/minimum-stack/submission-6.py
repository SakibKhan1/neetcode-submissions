class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val) 
        if self.minstack and val < self.minstack[-1]:
            self.minstack.append(val) 

    def pop(self) -> None:
        if self.stack and self.minstack: 
            s = self.stack.pop() 
            if s in self.minstack: 
                self.minstack.remove(s)

            

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]

