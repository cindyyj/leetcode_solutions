class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # @v_paliy note that:
        # "count[x] sorts by frequency, and if two values are equal, it will sort the keys in decreasing order."
        counts = Counter(nums)
        return sorted(nums, key=lambda x: (counts[x], -x))
        
        