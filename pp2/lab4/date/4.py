import datetime

date1 = datetime.datetime.today()
date2 = datetime.datetime(2005, 7, 2)
diff = date1 - date2
print(f"Difference beetween 2 dates in seconds: {diff.total_seconds()}")