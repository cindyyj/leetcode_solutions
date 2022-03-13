class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        # https://leetcode-cn.com/problems/maximum-population-year/solution/ren-kou-zui-duo-de-nian-fen-by-leetcode-5m7r4/
        # 「差分」+「前缀和」
        delta = defaultdict(int)
        for born, died in logs:
            delta[born] += 1
            delta[died] -= 1
        
        maxp = 0    # 人口数量最大值
        res = 0     # 最大值对应的最小下标
        curr = 0    # 每一年的人口数量
        
        # 前缀和 
        # cannot use for year in delta dictionary, the year is not ordered chronologically!!!
        for year in range(1950, 2051):
            curr += delta[year]
            if curr > maxp:
                maxp = curr
                res = year        
        return res
        

#         d = defaultdict(int)
#         for born, died in logs:
#             for year in range(born, died):
#                 d[year] += 1
        
#         max_alive = 0
#         res = 0
#         for year in range(1950, 2051):
#             alive = d[year]
#             if alive > max_alive:
#                 res = year
#                 max_alive = alive
            
#         return res