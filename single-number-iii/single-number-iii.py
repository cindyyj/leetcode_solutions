class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
# --------------------------- METHOD 1 ---------------------------
	# Use set to store numbers seen once, remove from set when seen twice. 
	# This method only works since you know you are going to see other numbers twice.
	# Memory Used: 16.4 MB
	# Runtime: 52 ms
    
        seen = set()
        
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                seen.remove(num)
        
        return list(seen)
    
# --------------------------- METHOD 2 ---------------------------
	# Use built-in list.count() method
	# Memory Used: 15.9 MB
	# Runtime: 4480 ms

#         single_list = list()
#         for num in nums:
#             if nums.count(num) == 1:
#                 single_list.append(num)
            
#         return single_list
