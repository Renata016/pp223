import datetime

today = datetime.datetime.today()
newdate = today.replace(microsecond = 0)
print(today)
print(newdate)