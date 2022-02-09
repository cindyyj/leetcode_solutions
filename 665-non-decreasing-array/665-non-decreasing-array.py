class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        # 错误: 直接判断是不是只出现了一次下降！[3,4,2,3]
        flag = True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if flag == False:
                    return False
                
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i + 1] = nums[i]
                
                flag = False
        return True