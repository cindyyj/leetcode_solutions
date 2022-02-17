class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. 
        # So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i
        # 当前 presum 与 K的关系，余数是几，当被除数为负数时取模结果为负数，需要纠正
        d = dict()
        d[0] = -1
        sums = 0

        for i in range(len(nums)):
            sums+=nums[i]
            if(k!=0):
                sums = sums%k
            if(sums in d):
                if(i-d[sums]>1):
                    return(True)
            else:
                d[sums] = i

        return False
    
#         pres = list(accumulate(nums))
#         d = Counter()
#         d[0] = -1
#         cnt = 0
        
#         for pre in pres:
#             key = (pre % k + k) % k
#             if key in d:
#                 cnt += d[key]
#             d[key] += 1
                
#         return cnt > 0        
    
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
