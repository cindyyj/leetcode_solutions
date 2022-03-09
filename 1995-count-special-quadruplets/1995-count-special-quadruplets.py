class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # https://leetcode-cn.com/problems/count-special-quadruplets/solution/tong-ji-te-shu-si-yuan-zu-by-leetcode-so-50e2/
        # walrus operator
        # b < c < d < n, c, d in [b + 1, n - 1]
        """
        我们将数组拆成红线分界的两个部分，左边包含a，b；右边包含c，d；
        我们直接遍历(a,b)，将产生n^2的复杂度；而对于c，d的差，我们不再继续叠加循环遍历；而是直接记录每一个可能的c，d的差的个数。
        每个遍历的b的位置都对应着上图中的一条分界线；c和d一定再右边；我们需要求的就是右边的区间里 d-c = a+b 的个数。

        这个区间个数怎么求呢？我们也可以用map来计数统计每个不同的cd之差对应的区间个数。
        如果我们遍历b的顺序是从右往左，则b每往左边移动一位，c就多出一个选择；所以我们只要让c成为b+1；从b+2位置往后遍历d的可能性，将不同的差枚举，并累计到差的计数map中即可。

        总体来说就是用O(n^2)O(n 
        2
         )的复杂度分别对ab之和还有dc之差做枚举；累加相等的数量。

        作者：wfnuser
        链接：https://leetcode-cn.com/problems/count-special-quadruplets/solution/wei-rao-li-lun-ha-xi-biao-liang-shu-zhi-b6f7p/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        
        # O(n**2) 2 loops
        n = len(nums)
        ans = 0
        cnt = Counter()
        for b in range(n - 3, 0, -1):
            for d in range(b + 2, n):
                cnt[nums[d] - nums[b + 1]] += 1
                
            for a in range(b):
                if (total := nums[a] + nums[b]) in cnt:
                    ans += cnt[total]
            
        return ans
    
        
#         # O(n**3) 3 loops
#         n = len(nums)
#         ans = 0
#         cnt = Counter()
        
#         for c in range(n - 2, 0, -1):
#             cnt[nums[c + 1]] += 1
#             for a in range(c):
#                 for b in range(a + 1, c):
#                     if (total := nums[a] + nums[b] + nums[c]) in cnt:
#                         ans += cnt[total]
                        
#         return ans