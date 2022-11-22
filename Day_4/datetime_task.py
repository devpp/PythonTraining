import datetime
import time
import calendar
from datetime import datetime as dt

d = datetime.datetime.now()

print(d)
print(d.year)
print(d.strftime("%A"))
print(d.strftime("%B"))

z = datetime.date(2017, 6, 19)
print(z)

today = datetime.date.today()

print("Year is ", today.year)
print("Month is ", today.month)
print("Date is ", today.day)

print(d.strftime("%a"))
print(d.strftime("%w"))
print(d.strftime("%d"))
print(d.strftime("%b"))
print(d.strftime("%m"))
print(d.strftime("%y"))
print(d.strftime("%Y"))
print(d.strftime("%H"))
print(d.strftime("%I"))
print(d.strftime("%p"))
print(d.strftime("%M"))