class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # https://leetcode.com/problems/top-k-frequent-elements/solution/
        # heap + Quickselect (Hoare's selection algorithm)
        
        freq = collections.Counter(nums)
        result = sorted(freq, key=lambda num: -freq[num])
        return result[:k]
        
        # return [x[0] for x in freq.most_common()[:k]]
        # c = Counter(nums)
        # return [x[0] for x in c.most_common()[:k]]    