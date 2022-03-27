class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = 6
        hour_angle = 30 
        
        mins = min_angle * minutes
        hours = (hour % 12 + minutes / 60) * hour_angle
        
        diff = abs(hours - mins)
        return min(diff, 360 - diff)