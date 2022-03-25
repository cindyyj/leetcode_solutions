class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # https://leetcode.com/problems/top-k-frequent-elements/solution/
        # heap + Quickselect (Hoare's selection algorithm)
        
        if k == len(nums):
            return nums
        
        cnt = Counter(nums)
        # heap for top k frequent O(nlogk)
        return heapq.nlargest(k, cnt.keys(), key=cnt.get)
        
        
        # freq = collections.Counter(nums)
        # # sort dict return sorted list of dict keys!!!
        # result = sorted(freq, key=lambda num: -freq[num])
        # return result[:k]
        
        # return [x[0] for x in freq.most_common()[:k]]
        # c = Counter(nums)
        # return [x[0] for x in c.most_common()[:k]]    