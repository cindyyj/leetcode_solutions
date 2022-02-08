class Solution:
    from collections import defaultdict
    
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