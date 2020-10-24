
# **** Time Delta ****

from datetime import datetime

for i in range(int(input())):
    t1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(abs(int((t1-t2).total_seconds())))



# **** Calendar Module ****

import datetime
import calendar

m, d, y = map(int, input().split())
input_date = datetime.date(y, m, d)
print(calendar.day_name[input_date.weekday()].upper())