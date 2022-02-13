class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # handle duplicate
        # replace the Hashmap <int, int> to Hashmap <int, Hashset> and pop the elements on the second loop.
        d = collections.defaultdict(list)
        for i, num in enumerate(nums2):
            d[num].append(i)
        return [d[num].pop() for num in nums1]    
        
        # won't work for duplicates!!!
        if sorted(nums1) != sorted(nums2):
            return False
        return [nums2.index(num) for num in nums1]