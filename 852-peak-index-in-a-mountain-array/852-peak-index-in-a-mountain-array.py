class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
#         # linear scan
#         # https://leetcode.com/problems/peak-index-in-a-mountain-array/discuss/139848/C%2B%2BJavaPython-Better-than-Binary-Search
#         return arr.index(max(arr))
        
        # linear scan with loop, Time, O(N)
        # The mountain increases until it doesn't. The point at which it stops increasing is the peak.
        for i in range(len(arr)):
            if arr[i] > arr[i+1]:
                return i
        
#         # binary search
#         l, r = 0, len(arr) - 1
#         while l <= r:
#             mid = l + (r-l) // 2
            
#             if arr[mid] > arr[mid+1] and arr[mid-1] < arr[mid]:
#                 return mid

#             if arr[mid] < arr[mid+1]:
#                 l = mid + 1
#             elif arr[mid] > arr[mid+1]:
#                 r = mid - 1
            
            
        