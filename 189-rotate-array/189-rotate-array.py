class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k% len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        
#         # 关于是否必须用 nums[:]：nums[:] = XX 的赋值，nums 的地址不变；
#         # nums = XX的赋值，nums 是新地址。在其他 IDE 试了试，如果return 输出一样就算正确的话，那不必须；
#         # 是 leetcode 的 IDE 直接调输入 nums 的地址，在def注释里写的
        
# #         When you do         lst = anything
# #         You're pointing the name lst at an object. It doesn't change the old object lst used to point to in any way, though if nothing else pointed to that object its reference count will drop to zero and it will get deleted.

# #         When you do         lst[:] = whatever
# #         You're iterating over whatever, creating an intermediate tuple, and assigning each item of the tuple to an index in the already existing lst object. That means if multiple names point to the same object, you will see the change reflected when you reference any of the names, just as if you use append or extend or any of the other in-place operations.
        
#         n = len(nums)        
#         k = k%n
        
#         nums[:] = nums[n-k:] + nums[:n-k]
        
# #         # Method 1 : list slicing
# #         k = k % len(nums)
# #         if len(nums) > 1 and k > 0:
# #             nums[:] = nums[-k:] + nums[:-k]
        
# #         # Method 2 : list replacing
# #         k = k % len(nums)
# #         if len(nums) > 1 and  k > 0:
# #             nums[:k], nums[k:] = nums[-k:], nums[:-k]
            
# #         # Method 3 : index assigning
# #         k = k % len(nums)
# #         tmp = nums[-k:]
# #         for index in range(len(nums)-1, k-1, -1):
# #             nums[index] = nums[index-k]
# #         for index, value in enumerate(tmp):
# #             nums[index] = value

# #         # Method 4 : reversed method
# #         k = k % len(nums)
# #         if len(nums) > 1 and  k > 0:
# #             nums[:] = reversed(nums)
# #             nums[:k], nums[k:] = reversed(nums[:k]), reversed(nums[k:])