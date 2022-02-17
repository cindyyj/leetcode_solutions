class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. 
        # So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i
        # 当前 presum 与 K的关系，余数是几，当被除数为负数时取模结果为负数，需要纠正
        # https://leetcode-cn.com/problems/continuous-subarray-sum/solution/de-liao-wo-ba-qian-zhui-he-miao-de-gan-g-c8kp/
        # 【动画模拟】一文秒杀七道题 程序厨
    
        if len(nums) <= 1:
            return False
        d = {0: -1}
        pre = 0
        for index, num in enumerate(nums):
            pre += num
            rem = pre % k
            i = d.get(rem, index)
            if i == index:
                d[rem] = index
            elif i <= index - 2:
                return True
        return False

# 作者：qingfengpython
# 链接：https://leetcode-cn.com/problems/continuous-subarray-sum/solution/523-lian-xu-de-zi-shu-zu-he-qian-zhui-he-zl78/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。        
#         pres = list(accumulate(nums))
#         d = defaultdict(int)
#         d[0] = -1
        
#         for i, pre in enumerate(pres):
#             key = pre % k
#             if key in d and i - d[key] > 1:
#                 return True
#             d[key] = i
                
#         return False   
    
        # For example for array [23,4,8] and k = 6 
        # we can see for indices 1 and 2 we have a subarray [4,8] which satisfies the constraint
        # sum([23,4]) = 27, 27 % 6 = 3
        # sum([23,4,6]) = 33 % 6 = 3
        # Which implies while iterating over the elements 
        # we have to store the mod of the prefix sum and whenever we encounter an existing mod we can return true

        ###### EXAMPLE ###############
        ### arr = [23,2,4,6,6], k= 7 ######
        # idx     n       prefix_sum  dict key=(prefix_sum%k), value=current_element_idx
        #                                 {0:-1}   # Initialization
        # 0      23          23           {0:-1, 2:0}
        # 1      2           25           {0:-1, 2:0, 4:1}
        # 2      4           29           {0:-1, 2:0, 4:1, 1:2}
        # 3      6           35           35%7 == 0, 0 was present in dict and idx - dict[0] > 1 ret True 
        # 4      6       
