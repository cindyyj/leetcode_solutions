class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Kth largest element in an array - Time: O(k + (n-k) log k), space: O(k)
        # minheap
        array = nums[:k]
        heapq.heapify(array) # O(k)
        for num in nums[k:]: # O(n-k)
            if num > array[0]:
                heapq.heapreplace(array, num) # O(log k)
        return array[0]
        
        # return heapq.nlargest(k, nums)[-1]   
        
        # return sorted(nums)[-k]