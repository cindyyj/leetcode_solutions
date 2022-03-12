class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        
        #  check how many numbers missing beween arr[0]
        # it's supposed to be 1, missing = arr[0] - 1 => arr[i] - (i + 1)
        # find a element whose missing is <= k using binary search        
        # check whether kth missing is at before 0th element || or after end element
        # if target not in arr, arr[bisect_left - 1] < target, insert at arr[bisect_left]
        # if target in or not in arr, arr[bisect_left] >= target
        # if target in or not in arr, arr[bisect_right] > target
        # if target not in arr, arr[bisect_left] == arr[bisect_right]
        
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            missing = arr[mid] - (mid + 1) # arr[i] should have i + 1 if no missing value
            
            # find lower bound (left boundary)
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        # return l + k
        
        missingLeft = arr[l-1] - l
        return arr[l-1] + (k - missingLeft)
    
    
# # --------------------------- METHOD 2  ---------------------------        
#         # 缺失的正整数一定 >= k
#         # 数组中每出现一个 <= k 的数字, 意味着少了一个缺失的数字, 此时k+1        
#         for i in arr:
#             if i <= k:
#                 k += 1
#         return k
    
# # --------------------------- METHOD 1 set ---------------------------
#         # use set to check if it contains a number (much faster!)
#         arr_set = set(arr)
#         for i in range(1, len(arr) + k + 1):
#             if i not in arr_set:
#                 k -= 1
#             if k == 0:
#                 return i

        """
        Lists are slightly faster than sets when you just want to iterate over the values.
        Sets, however, are significantly faster than lists if you want to check if an item is contained within it.
        They can only contain unique items though.
        
        Now, we have two good indicators, that we need to use binary search: sorted data and O(log n) complexity.
        
        https://leetcode.com/problems/kth-missing-positive-number/discuss/1004782/Python-Many-Solutions-4-LoC-O(log-n)-Follow-up-with-Explanation
        
        缺失的正整数一定 >= k
        数组中每出现一个 <= k 的数字, 意味着少了一个缺失的数字, 此时k+1
        
        """            