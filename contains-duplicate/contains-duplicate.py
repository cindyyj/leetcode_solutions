class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        
        
        # Method 1 -- Apply set 
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False

        # Method 2 -- Sorting
        # l =  len(nums)
        # if l < 2:
        #     return False
        # nums.sort()
        # for i in range(l-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

    #     # Method 3 -- Set solution for python
    #     return len(set(nums)) != len(nums)