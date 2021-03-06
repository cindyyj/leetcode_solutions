class MaxStack(list):
    def push(self, x: int) -> None:
        self.append((x, max(self.peekMax(), x) if self else x))
        
        
    def pop(self) -> int:
        return super().pop()[0]


    def top(self) -> int:
        return self[-1][0]
        

    def peekMax(self) -> int:
        return self[-1][1]
        

    def popMax(self) -> int:
        _stack = []
        while self.top() != self.peekMax():
            _stack.append(self.pop())
        
        r = self.pop()
        while _stack:
            self.push(_stack.pop())
        return r
    
    # use tuple to save max
    def __init__(self):
        self.stack = []        

    def push(self, x: int) -> None:
        m = max(x, self.peekMax()) if self.stack else x 
        self.stack.append((x, m))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]        

    def peekMax(self) -> int:
        return self.stack[-1][1]     

    def popMax(self) -> int:

        _cache = []
        cur_max = self.peekMax()
        while self.top() != self.peekMax():
            _cache.append(self.pop())
        
        self.stack.pop()
        while _cache:
            self.push(_cache.pop())
            
        return cur_max
     


    # Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()