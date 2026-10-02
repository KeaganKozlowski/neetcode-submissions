class MinStack:

    def __init__(self):
        self.stack = []
        self.store_min = [math.inf]
        print(self.store_min)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.store_min.append(min(val, self.store_min[-1]))
        
    def pop(self) -> None:
        self.stack.pop()
        self.store_min.pop()       

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.store_min[-1]

        
        
