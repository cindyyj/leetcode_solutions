class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        If p2 == 0, we've successfully merged nums2 into nums1. 
        Hence, we can return straightaway since there is nothing more to be done.
        If p1 == 0, we are only left with nums2 elements to fix. 
        Since we started with largest elements first, 
        we can guarantee that the remaining k elements in nums2 (where k <= n) are smaller than the rest of the elements we've previously fixed.
        """
        pointer1 = m-1
        pointer2 = n-1
        write_index = m+n-1
        
        while pointer2 >= 0:
            if pointer1 >=0 and nums1[pointer1] > nums2[pointer2]:
                nums1[write_index] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[write_index] = nums2[pointer2]
                pointer2 -= 1
        
            write_index -= 1 
