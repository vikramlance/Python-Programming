
from datetime import datetime, date


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_time_obj1 = datetime.strptime(date1, '%Y-%m-%d')
        date_time_obj2 = datetime.strptime(date2, '%Y-%m-%d')

        return abs(((date_time_obj1) - (date_time_obj2)).days)


date1 = "2019-06-29"
date2 = "2019-06-30"
test = Solution()

print(test.daysBetweenDates(date1, date2))
