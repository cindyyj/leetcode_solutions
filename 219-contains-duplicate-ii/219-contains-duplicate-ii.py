class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # sliding window + hashmap
        """
        This will work  in case of multiple duplicates? 1,0,1,1,2 and k =1 ??
        Because the index in the hashmap gets updated so the distance i - dic[j] will always reflect the shortest distance between deplicates.
        """
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap and i - hashmap[num] <= k:
                return True
            hashmap[num] = i
        
        return False         