class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # https://stackoverflow.com/questions/19480028/attributeerror-datetime-module-has-no-attribute-strptime
        # Timedelta objects have read-only instance attributes .days, .seconds, and .microseconds
        from datetime import datetime as dt

        return abs( dt.strptime(date2, "%Y-%m-%d").date() - dt.strptime(date1, "%Y-%m-%d").date()).days
        