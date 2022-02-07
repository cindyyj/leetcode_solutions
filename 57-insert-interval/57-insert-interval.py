class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # optimized
        # start, end
        s, e = newInterval[0], newInterval[1]
        
        left, right = [], []
        #  WRONG!!!
        # MISTAKE: Don't use multi-assignment for mutable object!!!
        # left = right = []
        
        for i in intervals:
            if i[1] < s:
                left.append(i)
                
            elif i[0] > e:
                right.append(i)
            
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        
        return left + [[s,e]] + right
        
#         # not optimized
#         intervals.append(newInterval)
#         intervals.sort(key=lambda x : x[0])
        
#         merged = []
#         for interval in intervals:
#             if not merged or merged[-1][1] < interval[0]:
#                 merged.append(interval)
                
#             else:
#                 merged[-1][1] = max(merged[-1][1], interval[1])
        
#         return merged