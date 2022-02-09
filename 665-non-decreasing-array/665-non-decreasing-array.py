class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        # 错误: 直接判断是不是只出现了一次下降！[3,4,2,3]
        """
        本题是要维持一个非递减的数列，所以遇到递减的情况时（nums[i] > nums[i + 1]），要么将前面的元素缩小，要么将后面的元素放大。

        但是本题唯一的易错点就在这，

        如果将nums[i]缩小，可能会导致其无法融入前面已经遍历过的非递减子数列；
        如果将nums[i + 1]放大，可能会导致其后续的继续出现递减；

        作者：Terry2020
        链接：https://leetcode-cn.com/problems/non-decreasing-array/solution/yi-ding-yao-rang-ni-nong-dong-wei-shi-ya-u9te/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        
        flag = True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:   # 要么缩小nums[i]，要么放大nums[i+1]
                if flag == False:  # going down 2nd time
                    return False
                
                if i == 0 or nums[i - 1] <= nums[i + 1]: 
                    nums[i] = nums[i+1] # 缩小nums[i]，因为nums[i+1]比nums[i-1]大
                else:
                    nums[i + 1] = nums[i] # 放大nums[i+1]，因为nums[i+1]太小了比nums[i-1]还小
                
                flag = False
        return True