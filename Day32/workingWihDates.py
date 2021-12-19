import datetime as dt

now = dt.datetime.now()
year = now.year
print(year)

date_of_birth = dt.datetime(day=23, month=6, year=1999, hour=5)

print(date_of_birth)

print(now.weekday())