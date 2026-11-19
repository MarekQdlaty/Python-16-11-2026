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

object_date = datetime.now().strptime("19/11/2026", "%d/%m/%Y")
print(object_date)  # 2026-11-19 00:00:00
print(type(object_date))  # <class 'datetime.datetime'>

# tomorrow = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2026-11-20

products = [
    {"sku": 1, "exp_date": today, "price": 100},
    {"sku": 2, "exp_date": today, "price": 100},
    {"sku": 3, "exp_date": tomorrow, "price": 100},
    {"sku": 4, "exp_date": today, "price": 100},
    {"sku": 5, "exp_date": today, "price": 100},
    {"sku": 6, "exp_date": tomorrow, "price": 100},
]
