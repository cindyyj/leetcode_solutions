class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # 假设油箱里的汽油可以为负数，找到最小的负数就是出发点
        # https://leetcode-cn.com/problems/gas-station/solution/jia-you-zhan-by-19216801-rt1i/
        """ 
        Every time a fail happens, accumulate the amount of gas that is needed to overcome the fail. 
        After looping through the stations, if the gas left is more than gas needed, then we have a solution, otherwise not.
        """
        gas_left = gas_needed = start = 0
        
        for i, (g, c) in enumerate(zip(gas, cost)):
            gas_left += g - c
            if gas_left < 0:
                gas_needed -= gas_left
                start = i + 1
                gas_left = 0
        return start if gas_left >= gas_needed else -1


        
#         n, spare, min_spare, min_idx = len(gas), 0, float('inf'), 0
        
#         for i in range(n):
#             spare += gas[i] - cost[i]  # total spare
#             if spare < min_spare:
#                 min_spare = spare
#                 min_idx = i 
            
#         return -1 if spare < 0 else (min_idx + 1) % n
