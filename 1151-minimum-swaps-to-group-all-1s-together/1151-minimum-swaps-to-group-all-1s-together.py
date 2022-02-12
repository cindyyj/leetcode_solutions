class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # 先数出一共有多少个1，输出来的个数就是窗口的长度
        # 定义需要维护的变量，求最小swap次数其实就是求窗口中0个数的最小值，因此定义num_zeros, min_num_zeros
        
        n = len(data)
        ones = 0
        for i in range(n):
            if data[i] == 1:
                ones += 1
        
        # special
        if ones <= 1:
            return 0
        
        # sliding window, length of ones
        start = 0
        zeros = 0
        minzeros = float('inf')
        
        for end in range(n):
            if data[end] == 0:
                zeros += 1
            
            if end >= ones - 1:
                minzeros = min(minzeros, zeros)
                if data[start] == 0:
                    zeros -= 1
                start += 1
        
        return minzeros