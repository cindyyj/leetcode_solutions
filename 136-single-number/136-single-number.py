from operator import xor

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
        
        # xor = 0
        # for num in nums:
        #     xor ^= num
        # return xor
        
        # return sum(set(nums)) * 2 - sum(nums)
        
# # --------------------------- METHOD 1 ---------------------------
# 	# Use dictionary to keep track of how many time each number appears
# 	# Memory Used: 16.7 MB
# 	# Runtime: 132 ms

# 		# num_dict = {num: 0 for num in nums}
# 		#
# 		# for num in nums:
# 		#     num_dict[num] += 1
# 		#
# 		# for num in nums:
# 		#     if num_dict[num]==1:
# 		#         return num


# # --------------------------- METHOD 2 ---------------------------
# 	# Use set to store numbers seen once, remove from set when seen twice. 
# 	# This method only works since you know you are going to see other numbers twice.
# 	# Memory Used: 16.7 MB
# 	# Runtime: 140 ms

# 		# seen = set()
# 		# for num in nums:
# 		#     if num in seen:
# 		#         seen.remove(num)
# 		#     else:
# 		#         seen.add(num)
# 		# return list(seen)[0]


# # --------------------------- METHOD 3 ---------------------------
# 	# Use built-in list.count() method
# 	# Memory Used: 16.5 MB
# 	# Runtime: >5 seconds

#         # for num in nums:
#         #     if nums.count(num) == 1:
#         #         return num


# # --------------------------- METHOD 4 ---------------------------
# 	# Use built-in list.sort() method
#         # for i in range(0,len(nums)-1,2):
#         #     if nums[i]!=nums[i+1]:
#         #         return nums[i]
#         # return nums[len(nums)-1]
        
#         nums.sort()
#         i = 0
#         while i < len(nums)-1:
#             if nums[i] != nums[i+1]:
#                 return nums[i]
#             i += 2
        
#         return nums[len(nums)-1]
    
