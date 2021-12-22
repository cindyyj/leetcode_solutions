class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        result = sorted(freq, key=lambda num: -freq[num])
        return result[:k]