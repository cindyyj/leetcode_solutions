import operator
from functools import reduce 

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(map(int, str(n)))
        return reduce(operator.mul, nums) - sum(nums)