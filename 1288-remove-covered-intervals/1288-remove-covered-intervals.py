class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Solution, sort left ascending and right decending
        # Sort by the left bound, and when left bounds are equal, sort right bounds by reverse order; 
        # Therefore, no interval can cover previous ones;
        # Loop through the intervals, whenever current right most bound < next interval's right bound, 
        # it means current interval can NOT cover next interval, update right most bound and increase counter by 1.
        # Time: O(nlogn), space: O(1) - excluding sorting space, where n = intervals.length.
        # https://leetcode.com/problems/remove-covered-intervals/discuss/451284/JavaPython-3-Simple-codes-w-explanation-and-analysis.
        
        count = cur = 0
        for _, r in sorted(intervals, key=lambda i: (i[0], -i[1])):
            if cur < r:
                cur = r
                count += 1
        return count