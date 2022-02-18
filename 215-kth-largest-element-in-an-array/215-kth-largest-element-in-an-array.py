class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Kth largest element in an array - Time: O(k + (n-k) log k), space: O(k)
        # minheap, maintain size k heap, top is kth largest element
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
        
        # return heapq.nlargest(k, nums)[-1]   
        
        # return sorted(nums)[-k]