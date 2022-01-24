from math import inf

class MinStack:

    # use same stack, push/pop twice if min needs update
    # use one constant to track min
    # O(2n) space, O(n)
    def __init__(self):
        self.stack = []
        self.min_stack = inf
        
    def push(self, val: int) -> None:
        if val <= self.min:
            self.stack.append(self.min) # push the last minimum in stack
            self.min = val
        self.stack.append(val) 

    def pop(self) -> None:
        pop_value = self.stack.pop() # pop once
        if pop_value == self.min:
            self.min_stack = self.stack.pop() # pop twice

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack if self.stack != inf else None
    
    
    # use tuple to save min
    #  using tuples as stack elements, that the second element in
    # the tuple is the min to enable constant getMin() 
    # O(2n) space, O(n)
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(self.getMin(), val)))   

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
    

#     # 辅助栈法
#     # keep another stack for min only 
#     # O(2n) space, O(n)
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []
        
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         # val <= self.min_stack[-1] won't work for cases of multiple same minimum, e.g. 3, 1, 1
#         if not self.min_stack or val <= self.min_stack[-1]: 
#             self.min_stack.append(val)        

#     def pop(self) -> None:
#         if self.stack[-1] == self.min_stack[-1]:
#             self.min_stack.pop()
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1] if self.stack else None

#     def getMin(self) -> int:
#         return self.min_stack[-1] if self.min_stack else None

        
# 面试的时候被问到不能用额外空间，就去网上搜了下不用额外空间的做法。思路是栈里保存差值。
# https://github.com/cissieAB/Udemy_LeetCodeInPython/blob/afb07219215250401d97de00a2592a54a1ca2e27/Codes/min_stack.py

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()