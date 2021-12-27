class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        single_list = list()
        for num in nums:
            if nums.count(num) == 1:
                single_list.append(num)
            
        return single_list
        