class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 253. Meeting Rooms II
        # 731. My Calendar II
        # 732. My Calendar III
        # 1094. Car Pooling
        # 1109. Corporate Flight Bookings
        # 218. The Skyline Problem
        # https://leetcode.com/problems/car-pooling/discuss/867628/3-different-approaches-in-Python.
        
        # bucket sort
        people = [0] * 1001
        for n, a, b in trips:
            people[a] += n
            people[b] -= n
            
        for cur in accumulate(people):
            if cur > capacity:
                return False
        return True

        
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
        
#         return maxp <= capacity