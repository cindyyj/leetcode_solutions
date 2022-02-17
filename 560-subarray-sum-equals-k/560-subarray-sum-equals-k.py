from itertools import accumulate
from collections import defaultdict

class Solution:
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        cur_sum = 0
        res = 0
        
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in prefix_sum:
                res += prefix_sum[cur_sum - k]
            
            prefix_sum[cur_sum] += 1
        
        return res
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
        
#         # num_times 存储某“前缀和”出现的次数，这里用collections.defaultdict来定义它
#         # 如果某前缀不在此字典中，那么它对应的次数为0
#         num_times = collections.defaultdict(int)
#         num_times[0] = 1  # 先给定一个初始值，代表前缀和为0的出现了一次
#         cur_sum = 0  # 记录到当前位置的前缀和
#         res = 0
#         for i in range(len(nums)):
#             cur_sum += nums[i]  # 计算当前前缀和
#             if cur_sum - k in num_times:  # 如果前缀和减去目标值k所得到的值在字典中出现，即当前位置前缀和减去之前某一位的前缀和等于目标值
#                 res += num_times[cur_sum - k]
#             # 下面一句实际上对应两种情况，一种是某cur_sum之前出现过（直接在原来出现的次数上+1即可），
#             # 另一种是某cur_sum没出现过（理论上应该设为1，但是因为此处用defaultdict存储，如果cur_sum这个key不存在将返回默认的int，也就是0）
#             # 返回0加上1和直接将其置为1是一样的效果。所以这里统一用一句话包含上述两种情况
#             num_times[cur_sum] += 1
#         return res

# # 作者：LotusPanda
# # 链接：https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/xiong-mao-shua-ti-python3-qian-zhui-he-zi-dian-yi-/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。