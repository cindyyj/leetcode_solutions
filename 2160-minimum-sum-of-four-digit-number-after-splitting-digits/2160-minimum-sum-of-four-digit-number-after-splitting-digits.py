class Solution:
    def minimumSum(self, num: int) -> int:
        arr = sorted(str(num))
        return int(arr[0] + arr[2]) + int(arr[1] + arr[3])