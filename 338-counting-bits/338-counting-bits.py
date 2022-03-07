class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # Brian Kernighan 算法,   这个算法的意思是，对任何一个数 n&(n−1)的结果是 n的比特位最右端的1变为0的结果
        
        def countOnes(num):
            ones = 0
            while num > 0:
                num &= (num - 1)
                ones += 1
            return ones
        
        bits = [countOnes(i) for i in range(n + 1)]
        return bits