from collections import deque

class MovingAverage:
    
    def __init__(self, size:int):
        self.size = size
        self.q = deque()
        self.window_sum = 0
        self.total_len = 0
    
    def next(self, val: int) -> float:
        self.total_len += 1
        
        self.q.append(val)
        
        tail = self.q.popleft() if self.total_len > self.size else 0
        self.window_sum += (val - tail)
        
        return self.window_sum / min(self.total_len, self.size)

#     # use queue
#     # time: O(window_size), retrieve last n=window_size to calculate the moving average
#     # space: O(M), total length of data feeds
#     def __init__(self, size: int):  
#         self.size = size
#         self.queue = [] #  initialize a variable queue to store the values from the data stream
        

#     def next(self, val: int) -> float:
#         size, queue = self.size, self.queue
#         queue.append(val)
#         window_sum = sum(queue[-size:])  # -k will not make index out of range!!! 
        
#         return window_sum/ min(len(queue), size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)