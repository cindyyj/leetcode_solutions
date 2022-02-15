# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.queue = collections.deque()

    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            buf4 = [''] * 4 
            _ = read4(buf4) 
            self.queue.extend(buf4)
            count = min(len(self.queue), n-i) 
            if not count:
                break
            buf[i:] = [self.queue.popleft() for _ in range(count)]
            i += count
        return i        