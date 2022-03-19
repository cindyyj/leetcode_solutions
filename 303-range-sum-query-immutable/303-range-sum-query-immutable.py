from itertools import accumulate 
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums     
        self.pres = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pres[right]
        else:
            return self.pres[right] - self.pres[left - 1]

    """
    advanced, 307. Range Sum Query - Mutable

    Time:
    Constructor: O(N)
    sumRange(left, right): O(1)
    Space: O(1)
    """

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)