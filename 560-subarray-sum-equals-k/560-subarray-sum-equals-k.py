from itertools import accumulate
from collections import defaultdict, Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pres = list(accumulate(nums))
        d = Counter()
        d[0] = 1  ### important to initialize d[0] = 1 to handle case like [1,1,1], k =2 
        cnt = 0
        
        for i, pre in enumerate(pres):
            if pre - k in d:
                cnt += d[pre-k]
            d[pre] += 1
        
        return cnt
            
    
    
#     def subarraySum(self, nums: List[int], k: int) -> int:        
#         prefix_sum = defaultdict(int)
#         prefix_sum[0] = 1
#         cur_sum = 0
#         res = 0
        
#         for i in range(len(nums)):
#             cur_sum += nums[i]
#             if cur_sum - k in prefix_sum:
#                 res += prefix_sum[cur_sum - k]
            
#             prefix_sum[cur_sum] += 1        
#         return res
    
    
# Just wanted to share a clear explanation that helped me.

# First of all, the basic idea behind this code is that, whenever the sums has increased by a value of k, we've found a subarray of sums=k.
# I'll also explain why we need to initialise a 0 in the hashmap.
# Example: Let's say our elements are [1,2,1,3] and k = 3.
# and our corresponding running sums = [1,3,4,7]
# Now, if you notice the running sums array, from 1->4, there is increase of k and from 4->7, there is an increase of k. So, we've found 2 subarrays of sums=k.

# But, if you look at the original array, there are 3 subarrays of sums==k. Now, you'll understand why 0 comes in the picture.

# In the above example, 4-1=k and 7-4=k. Hence, we concluded that there are 2 subarrays.
# However, if sums==k, it should've been 3-0=k. But 0 is not present in the array. To account for this case, we include the 0.
# Now the modified sums array will look like [0,1,3,4,7]. Now, try to see for the increase of k.

# 0->3
# 1->4
# 4->7
# Hence, 3 sub arrays of sums=k        
        
        # num_times for 
        # collections.defaultdict can handle missing value, missing value = 0 
        # A call to a built-in type like (empty) list, set, dict, str,  (zero) int, or float will return an empty object or zero for numeric types.
        
#         # num_times ???????????????????????????????????????????????????collections.defaultdict????????????
#         # ???????????????????????????????????????????????????????????????0
#         num_times = collections.defaultdict(int)
#         num_times[0] = 1  # ?????????????????????????????????????????????0??????????????????
#         cur_sum = 0  # ?????????????????????????????????
#         res = 0
#         for i in range(len(nums)):
#             cur_sum += nums[i]  # ?????????????????????
#             if cur_sum - k in num_times:  # ??????????????????????????????k????????????????????????????????????????????????????????????????????????????????????????????????????????????
#                 res += num_times[cur_sum - k]
#             # ??????????????????????????????????????????????????????cur_sum???????????????????????????????????????????????????+1????????????
#             # ???????????????cur_sum????????????????????????????????????1????????????????????????defaultdict???????????????cur_sum??????key???????????????????????????int????????????0???
#             # ??????0??????1?????????????????????1???????????????????????????????????????????????????????????????????????????
#             num_times[cur_sum] += 1
#         return res

# # ?????????LotusPanda
# # ?????????https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/xiong-mao-shua-ti-python3-qian-zhui-he-zi-dian-yi-/
# # ??????????????????LeetCode???
# # ??????????????????????????????????????????????????????????????????????????????????????????????????????