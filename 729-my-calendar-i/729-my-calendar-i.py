from sortedcontainers import SortedList

class MyCalendar:
    # brute force
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        
        #  two events [s1, e1) and [s2, e2) do not conflict 
        # if and only if one of them starts after the other one ends: 
        # either e1 <= s2 OR e2 <= s1. 
        # By De Morgan's laws, this means the events conflict when s1 < e2 AND s2 < e1.

        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True
    
#     # sorted list
#     # https://leetcode.com/problems/my-calendar-i/discuss/1262532/Python-Sortedlist-solution-explained    
#     def __init__(self):
#         self.arr = SortedList()        

#     def book(self, start: int, end: int) -> bool:
#         q1 = SortedList.bisect_right(self.arr, start)
#         q2 = SortedList.bisect_left(self.arr, end)
#         if q1 == q2 and q1 % 2 ==0:
#             self.arr.add(start)
#             self.arr.add(end)
#             return True
#         return False        



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)