class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 253. Meeting Rooms II
        # 731. My Calendar II
        # 732. My Calendar III
        # 1094. Car Pooling
        # 1109. Corporate Flight Bookings
        # 218. The Skyline Problem
        # https://leetcode.com/problems/car-pooling/discuss/867628/3-different-approaches-in-Python.

        # Meeting Rooms II (Sorting all intervals)4
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
            
        # The sort() method is used to sort the elements in ascending order and by default
        # for list of tuples, it will sort the first element. 
        # If two tuples have the same first element then it will sort them according to the second element.
        lst.sort()
        return not any(n > capacity for n in accumulate(map(lambda x:x[1], lst)))
        
        # pas = 0
        # for loc in lst:
        #     pas += loc[1]
        #     if pas > capacity:
        #         return False
        # return True
    
#         stops = sorted([k for n, a, b in trips for k in ((a, n), (b, -n))])
#         return not any(n > capacity for n in accumulate(map(lambda x: x[1], stops)))        
        
#         # bucket sort
#         people = [0] * 1001
#         for n, a, b in trips:
#             people[a] += n
#             people[b] -= n
            
#         for cur in accumulate(people):
#             if cur > capacity:
#                 return False
#         return True

        
#         # 前缀和 prefix sum
#         d = defaultdict(int)
        
#         for num, start, end in trips:
#             d[start] += num
#             d[end] -= num
        
#         maxp = 0
#         total = 0
        
#         #  sorted(d) -> sort dict by key, defaultdict do not have attribute sort! 
#         for pos in sorted(d):
#             total += d[pos]
#             d[pos] = total
#             maxp = max(d[pos], maxp)
#             if maxp > capacity:
#                 return False
        
#         return True # maxp <= capacity