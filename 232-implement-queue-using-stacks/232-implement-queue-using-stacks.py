class MyQueue:

    def __init__(self):
        """
        in主要负责push，out主要负责pop
        """
        self.stackin = []
        self.stackout = []

    def push(self, x: int) -> None:
        """
        有新元素进来，就往in里面push
        """
        self.stackin.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None
        
        if self.stackout:
            return self.stackout.pop()
    
        else:
            for _ in range(len(self.stackin)):
                self.stackout.append(self.stackin.pop())
            return self.stackout.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        ans = self.pop()
        self.stackout.append(ans)
        return ans

    def empty(self) -> bool:
        """
        只要in或者out有元素，说明队列不为空
        """        
        return not (self.stackin or self.stackout)
        

# 链接：https://leetcode-cn.com/problems/implement-queue-using-stacks/solution/dai-ma-sui-xiang-lu-dai-ni-gao-ding-zhan-6ngt/

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()