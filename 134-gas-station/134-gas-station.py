class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # 假设油箱里的汽油可以为负数，找到最小的负数就是出发点
        # https://leetcode-cn.com/problems/gas-station/solution/jia-you-zhan-by-19216801-rt1i/
        
        n = len(gas)
        cur_gas = min_gas = min_idx = 0 # start from 0
        
        for i in range(n):
            cur_gas += gas[i] - cost[i]
            if cur_gas < min_gas:
                min_gas = cur_gas
                min_idx = i + 1  # 这里i如果是n-1的话，说明当前汽油比0小，返回-1,不会返回错误的n。
        
        return min_idx if cur_gas >= 0 else -1
        
        
        
        
#         n, spare, min_spare, min_idx = len(gas), 0, float('inf'), 0
        
#         for i in range(n):
#             spare += gas[i] - cost[i]  # total spare
#             if spare < min_spare:
#                 min_spare = spare
#                 min_idx = i 
            
#         return -1 if spare < 0 else (min_idx + 1) % n
        