class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        # Hashmap
        # setdefault() method returns the value of the item with the specified key.
        # If the key does not exist, insert the key, with the specified value, see example below
        
        map_ = {}
        # 将其存入哈希表中，含义为，若该元素不存在则存入表中，并计数为1，若已经存在获取次数并加1
        for x in nums:
            
            map_.setdefault(x, 0)
            map_[x] += 1
        # 遍历出出现次数为1的情况
        
        return [num for num, count in map_.items() if count == 1]
    
        # for y, count in map_.items():
        #     if count == 1:
        #         return y
    

# --------------------------- METHOD 3 ---------------------------        
#         c = collections.Counter(nums)
#         return [num for num, count in c.items() if count == 1]
        
# --------------------------- METHOD 2 ---------------------------
	# Use set to store numbers seen once, remove from set when seen twice. 
	# This method only works since you know you are going to see other numbers twice.
	# Memory Used: 16.4 MB
	# Runtime: 52 ms
    
#         seen = set()
        
#         for num in nums:
#             if num not in seen:
#                 seen.add(num)
#             else:
#                 seen.remove(num)
        
#         return list(seen)
    
# --------------------------- METHOD 1 ---------------------------
	# Use built-in list.count() method
	# Memory Used: 15.9 MB
	# Runtime: 4480 ms

#         single_list = list()
#         for num in nums:
#             if nums.count(num) == 1:
#                 single_list.append(num)
            
#         return single_list


    
        