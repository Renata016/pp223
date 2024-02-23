import datetime

def FiveDaysAgo():
    current = datetime.datetime.now()
    new = current.day - 5
    return new

print(FiveDaysAgo())