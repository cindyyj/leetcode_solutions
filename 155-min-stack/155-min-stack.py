class MinStack:

    # 辅助栈法
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)        

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()       

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
# 面试的时候被问到不能用额外空间，就去网上搜了下不用额外空间的做法。思路是栈里保存差值。
# https://github.com/cissieAB/Udemy_LeetCodeInPython/blob/afb07219215250401d97de00a2592a54a1ca2e27/Codes/min_stack.py

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()