class Logger:
    def __init__(self):
        # queue of messages received in last 10 seconds
        self.msg_q = collections.deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # delete older elements to keep window of 10 seconds
        while self.msg_q and timestamp - self.msg_q[0][0] >= 10:
            self.msg_q.popleft()
        
        # if message is found in window, cannot print it
        # great example of any
        if any(message in msg for t, msg in self.msg_q): 
            return False
        
        # if not in window, append to queue
        self.msg_q.append((timestamp, message))
        return True

# class Logger:

#     def __init__(self):
#         self.msg_dict = {}
        

#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
#         if message not in self.msg_dict:
#             self.msg_dict[message] = timestamp
#             return True
        
#         if timestamp - self.msg_dict[message] >= 10:
#             self.msg_dict[message] = timestamp
#             return True
#         else:
#             return False

"""
case 1). we have never seen the message before.
case 2). we have seen the message before, and it was printed more than 10 seconds ago.

hashmap solution, time O(1) lookup and update hashtable is constant time. space O(m), m is size of all msgs
    cons: But for a Logger, probably it not that practical. Since your HashMap soon will blew up ....
"""
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)