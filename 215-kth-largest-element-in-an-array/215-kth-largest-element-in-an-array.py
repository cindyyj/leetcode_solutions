class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Kth largest element in an array - Time: O(k + (n-k) log k), space: O(k)
        # minheap, maintain size k heap, top is kth largest element
        # queue = nums[:k]
        # heapq.heapify(queue)
        # for num in nums[k:]:
        #     heapq.heappushpop(queue, num)
        #     # heapq.heappush(queue, num)
        #     # heapq.heappop(queue)
        # return queue[0]
        
        return heapq.nlargest(k, nums)[-1]   
        
        # return sorted(nums)[-k]