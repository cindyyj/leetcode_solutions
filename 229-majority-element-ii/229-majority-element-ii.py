class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Moore Voting (Match 3 Game)
        
        num1, num2, freq1, freq2 = None, None, 0, 0
        
        for num in nums:
            if num == num1: # 统计A的个数
                freq1 += 1
            elif num == num2: # 统计B的个数
                freq2 += 1
            elif freq1 == 0: # A还没有，给他赋值
                num1, freq1 = num, 1
            elif freq2 ==0: # B还没有，给他赋值
                num2, freq2 = num, 1
            else:
                # 到这里说明A和B都有了，并且这里出现了
                # 一个不是A或B的值。
                # 只有出现3个不同数字的时候，他们
                # 才能同时销毁
                freq1 -= 1
                freq2 -= 1
        #at this point, we have two elements with maximum frequency
        #now we need to check the frequency of these two elements, if the particular elements appear more than n//3 times
        
        return [num for num in [num1, num2] if nums.count(num) > len(nums) // 3]

        
#         # set, very slow
#         # Runtime: 234 ms, faster than 5.10% of Python3 online submissions for Majority Element II.
#         # Memory Usage: 15.4 MB, less than 31.90% of Python3 online submissions for Majority Element II.
#         unique = set(nums)
#         return [num for num in unique if nums.count(num) > len(nums) / 3]

#         # HashMap
#         counts = collections.Counter(nums)
#         ans = []
        
#         for key, value in counts.items():
#             if value > len(nums)/3:
#                 ans.append(key)                
#         return ans
        
#         # Brute Force: Time (O(n**2))
#         majority_count = len(nums) // 3
#         seen = []
#         ans = []
#         for num in nums:
#             if num not in seen:
#                 count = sum([1 for elem in nums if elem == num])
#                 if count > majority_count:
#                     ans.append(num)
#                     seen.append(num)        
#         return ans