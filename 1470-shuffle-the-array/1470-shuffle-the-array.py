class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        lst = []
        for i in range(n):
            lst.append(nums[i])
            lst.append(nums[n + i])
        return lst
        
        # res = [0] * 2 * n
        # for i in range(n):
        #     res[i*2] = nums[i]
        #     res[i*2 + 1] = nums[n + i]
        # return res        