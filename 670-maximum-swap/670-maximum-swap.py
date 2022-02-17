class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(nums)}
        
        for i in range(len(nums)):
            for d in range(9, nums[i], -1):
                if last.get(d, -1) > i:
                    nums[i], nums[last[d]] = nums[last[d]], nums[i]
                    return int("".join(map(str, nums)))
        return num
                    
  

    """
    从左往右枚举每个位上的数字，找到比当前数字大且最大，最靠右(最低位)的数字，进行交换。没有则不交换

    //找到相同值最后出现的位置
    //原数组从左到右遍历，索引数组从后往前遍历
    //遇到比当前位值大的，交换，因为索引数组从后往前遍历的，所以保证了值为最大

    举几个例子先：

    2736：2找到后面最大的7\U0001f449交换\U0001f4497236
    98368：9后面没有比它大的，8也是。3找到后面最大的8\U0001f449交换\U0001f44998863
    1993：这个例子就体现最靠右，1找到后面最大的9，而且要是最靠右的9\U0001f449交换\U0001f4499913（❌9193）
    3997: 9937

    作者：Ben_
    链接：https://leetcode-cn.com/problems/maximum-swap/solution/xiang-jie-yong-bao-li-mei-ju-tan-xin-ko6-wj3g/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """