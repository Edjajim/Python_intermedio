### Fechas ###

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

programer_day = datetime(2023, 9, 13)

print_date(programer_day)

from datetime import time

current_time = time(16, 30, 23)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday())

current_date = date(2023, 9, 13)

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday())

current_date = date(current_date.year, current_date.month  + 1, current_date.day)

print(current_date)

diff = programer_day - now
print(diff)

diff = programer_day.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(208, weeks=7)
end_timedelta = timedelta(300, weeks=2)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)