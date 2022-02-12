from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # hashmap
        return sum(num for num, cnt in Counter(nums).items() if cnt == 1)
        