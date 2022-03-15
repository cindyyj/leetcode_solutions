class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        # bisect.insort(arr, x, lo=0, hi=len(a), *, key=None)
        # Similar to insort_left(), but inserting x in arr after any existing entries of x.
        # The insort() functions are O(n) because the logarithmic search step is dominated by the linear time insertion step!!!
        
        d = collections.defaultdict(list)
        for student, score in items:
            bisect.insort(d[student], score)
        return [[i, sum(sorted(d[i])[-5:]) // 5] for i in sorted(d)]        
        
        
        
        
#         scores = defaultdict(list)
        
#         for i, score in items:
#             scores[i].append(score)
        
#         ans = []
#         for i in sorted(scores):
#             ans.append([i, sum( sorted(scores[i], reverse=True)[:5] ) // 5])
        
#         return ans