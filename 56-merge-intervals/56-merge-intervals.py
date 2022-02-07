class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # https://leetcode.com/problems/merge-intervals/solution/
        # official leetcode solution 
        # classic!!! 
        
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
                
            else:
                # updated right end of last interval
                merged[-1][1] = max(interval[1], merged[-1][1])
        
        return merged
# # 链接：https://leetcode-cn.com/problems/merge-intervals/solution/he-bing-qu-jian-by-leetcode-solution/
