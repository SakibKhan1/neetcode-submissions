from collections import deque 
class MyStack:

    def __init__(self):
        self.queue1 = deque() 
        self.queue2 = deque() 

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if len(self.queue1) >= 1:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.popleft())
        if len(self.queue1) == 1:
            s = self.queue1.popleft() 
        for _ in range(len(self.queue2)):
            self.queue1.append(self.queue2.popleft())
        return s 

    def top(self) -> int:
        if len(self.queue1) >= 1:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.popleft())
        if len(self.queue1) == 1:
            res = self.queue1.popleft() 
        self.queue2.append(res) 
        for _ in range(len(self.queue2)):
            self.queue1.append(self.queue2.popleft())

        return res 

    def empty(self) -> bool:
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return True 
        else:
            return False 



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()