# calendar, dateutils
from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2026-11-19

time = datetime.now()
print(time)  # 2026-11-19 11:12:41.482838

print(type(today))  # <class 'datetime.date'>
print(type(time))  # <class 'datetime.datetime'>

print(today.day)  # 19
# Return day of the week, where Monday == 0 ... Sunday == 6.
print(today.weekday())  # 3
# Return day of the week, where Monday == 1 ... Sunday == 7.
print(today.isoweekday())  # 4
