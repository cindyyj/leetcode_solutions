class Solution:
    def dayOfYear(self, date: str) -> int:
        # Have a integer array of how many days there are per month. 
        # February gets one extra day if its a leap year.
        # Then, we can manually count the ordinal as day + (number of days in months before this one).


        y, m, d = map(int, date.split('-'))
#         days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
#         # leap year
#         if ( (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0))): 
#             days[1] = 29
        
#         return d + sum(days[:m-1])
    
        return int((datetime.datetime(y, m, d) - datetime.datetime(y, 1, 1)).days + 1)