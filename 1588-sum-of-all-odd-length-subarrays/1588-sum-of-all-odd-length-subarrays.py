from itertools import accumulate

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        """
        根据题意逐步计算子数组的和，发现每个数字都多次出现，多次计算，故思考能否直接计算每个数字的出现次数，思路如下：
        1.任取数组下标为i(第i+1个)的元素
        2.其左边可以取0~i个元素，共i+1种方案，其中(i+1)/2种为奇数，i/2+1种为偶数
        3.右边可以取0~(n-i-1)个元素，共n-i种方案，其中(n-i)/2种为奇数，(n-i+1)/2种为偶数
        4.合成子数组须满足条件：左边+本身+右边 = 奇数个，故左奇->右奇，左偶->右偶
        5.所以arr[i]的出现次数为lOdd X rOdd + lEven X rEven，即左奇X右奇 + 左偶X右偶
        注：不会出现所谓的重复统计，因为每次都计算不同数字的出现次数

        作者：shaw-r
        链接：https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/solution/tong-ji-yuan-su-chu-xian-ci-shu-yi-ci-bian-li-0mss/
        """
        total = 0
        n = len(arr)
        prefix = [0] + list(accumulate(arr))
        for length in range(1, n + 1, 2):
            for start in range(n - length + 1):
                total += prefix[start + length] - prefix[start]
        return total

# # --------------------------- METHOD 2 ---------------------------    
#         # math, O(n), best
#         res = 0
#         n = len(arr)
#         for i, v in enumerate(arr):
#             leftCount, rightCount = i, n - i - 1
#             leftOdd = (leftCount + 1) // 2
#             rightOdd = (rightCount + 1) // 2
#             leftEven = leftCount // 2 + 1
#             rightEven = rightCount // 2 + 1
#             res += v * (leftOdd * rightOdd + leftEven * rightEven)
#         return res
            
# --------------------------- METHOD 3 ---------------------------            
#         # brute force (AC), time O (n**3)
#         total = 0
#         n = len(arr)
        
#         for length in range(1, n + 1, 2):
#             for start in range(n - length + 1):
#                 total += sum(arr[start : start + length])
        
#         return total