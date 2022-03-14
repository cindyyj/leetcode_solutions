class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Great solution! Mine was a little more general but slower
        # using math.comb. Of course you can change 2 to choose k items in general (Python docs).

        return sum([math.comb(n, 2) for n in collections.Counter(nums).values()])