class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
            Keep two lists a left and a right list
            
            in the left list, keep running product of everything to the left
            
            int the right list, keep running product of everything to the right
            
            combine at the end
            
            O(N) time and space complexity
        """
        length = len(nums)
        
        left_products = [1] * length
        right_products = [1] * length
        combined_products = [0] * length
        
        # Build left products
        for i in range(1, length):
            left_products[i] = nums[i-1] * left_products[i-1]
            
        # Build right products
        for i in range(length -2, -1, -1):
            right_products[i] = nums[i+1] * right_products[i+1]
        
        # Combine product lists together
        for i in range(length):
            combined_products[i] = left_products[i] * right_products[i]
            
        return combined_products
    
#     # --------------------------- METHOD 1 ---------------------------
        
#         zero_count = nums.count(0)
#         if zero_count > 1:
#             return [0] * len(nums)
        
#         if zero_count == 1:
#             # product
#             p = 1
#             for i in range(len(nums)):
#                 if nums[i] == 0:
#                     idx = i 
#                 else:
#                     p *= nums[i]
#             res = [0] * len(nums)
#             res[idx] = p
#             return res 
            
#         if zero_count == 0:
#             p = 1
#             for i in range(len(nums)):
#                 p *= nums[i]
#             return [p//num for num in nums]