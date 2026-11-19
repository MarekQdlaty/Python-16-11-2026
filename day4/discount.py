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

# formatowanie dat
print(today.strftime("%A"))  # Thursday

formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 19/11/2026
print(type(formated_date))  # <class 'str'>

# 11:18
# 11:18:45
# 11:18 am

# formated_time = datetime.now().strftime("%H:%M")
# formated_time = datetime.now().strftime("%H:%M:%S") # 11:24:12
formated_time = datetime.now().strftime("%I:%M:%S %p")  # 11:24:40 AM
print(formated_time)  # 19/11/2026
print(type(formated_time))
