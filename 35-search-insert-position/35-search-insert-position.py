class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        nums.append(target)
        nums.sort() # Timsort, sorting will take O(nlogn) time.
        return nums.index(target)  # num.index() time O(n)
        
#         # binary search no duplicate, stop when l > r
#         # 循环结束后，在left和right之间画一条竖线，恰好可以把数组分为两部分：
#         # left左边的部分和right右边的部分，而且left左边的部分全部小于target，并以right结尾；
#         # right右边的部分全部大于等于target，并以left为首。所以最终答案一定在left的位置。
#         # 在while循环开始之前，其实可以简单做做一下判断，
#         # 如果target比nums中所有的数都小，直接返回0；如果比nums中所有的数全部大，返回len，循环就不用考虑边界了，逻辑会清晰很多
        
#         l , r = 0, len(nums)-1
#         while l <= r:
#             mid=l + (r - l) // 2 #prevent overflow
#             if nums[mid]== target:
#                 return mid
#             if nums[mid] < target:
#                 l = mid+1
#             else:
#                 r = mid-1
#         return l
    
#         # 由题意，无论target在不在有序列表中，只需要得到比target小的数的个数即为target索引。
#         # Time: O(n), Space O(n)
#         return len( [x for x in nums if x < target])

