class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        # popular in google
        # O(n) linear time if array pre-sorted, otherwise need to sort, O(nlogn)
        # timeSeries sorted! as non-decreasing
        
        # Iterate over timeSeries list. 
        # At each step add to the total time the minimum between interval length and the poisoning time duration duration.
        
        # 我们记录艾希恢复为未中毒的起始时间 expired，
        # 设艾希遭遇第 i 次的攻击的时间为 timeSeries[i]

        # 作者：LeetCode-Solution
        # 链接：https://leetcode-cn.com/problems/teemo-attacking/solution/ti-mo-gong-ji-by-leetcode-solution-6p4k/

        # total time in poisoned status
        # expired, the start time in non-poison status
        total, expired = 0, 0 
        for i in range(len(timeSeries)):
            if timeSeries[i] >= expired:
                total += duration
            else:
                total += timeSeries[i] + duration - expired
            expired = timeSeries[i] + duration
        
        return total