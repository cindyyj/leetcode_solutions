class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. 
        # So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i
        # 当前 presum 与 K的关系，余数是几，当被除数为负数时取模结果为负数，需要纠正
        seen, cur = {0: -1}, 0
        for i, a in enumerate(nums):
            cur = (cur + a) % abs(k) if k else cur + a
            if i - seen.setdefault(cur, i) > 1: return True
        return False   
    
#         if len(nums) <= 1:
#             return False
        
#         pres = list(accumulate(nums))
#         d = defaultdict(int)
#         d[0] = -1
#         cnt = 0
        
#         for i, pre in enumerate(pres):
#             key = pre % k
#             if key in d and i - d[key] > 1:
#                 return True
    
#             d[key] = i
                
        return False   
    
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
