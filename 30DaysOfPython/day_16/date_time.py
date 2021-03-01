#Examples
'''
import datetime
print(dir(datetime))

from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')

from datetime import datetime
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time_one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time two:", time_two)

from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current_day:", today.day)

from datetime import time
a = time()
print("a=", a)
b = time(10, 30, 50)
print("b= ", b)
c = time(hour=10, minute=30, second=50)
print("c= ", c)
d = time(10, 30, 50, 20055)
print("d =", d)

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
'''
#Exercise
#Problem 1
from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute, timestamp)

#Problem 2
from datetime import datetime
now = datetime.now()
time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time)

#Problem 3
from datetime import datetime
time_string = "5 December, 2019"
time = datetime.strptime(time_string, "%d %B, %Y")
print(time)

#Problem 4
from datetime import datetime
now = datetime(year = 2021, month = 3, day = 1, hour = 17, minute = 49, second = 0)
new_year = datetime(year = 2022, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = new_year - now
print('Time left for new year:', diff)

#Problem 5
from datetime import date
then = date(day = 1, month = 1, year = 1970)
now = date(day = 1, month = 3, year = 2021)
diff = now - then
print(diff)


