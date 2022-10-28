import datetime as dt

now = dt.datetime.today()

print(now.year)
print(now.month)
print(now.day)
print(now.date())

myDate = now.date()

for i in range(14, 140, 14):
   myDate = myDate + dt.timedelta(days=i)
   print(myDate)

birth = dt.date(2022, 10, 3)
today = dt.date.today()
difference = today - birth

print(difference)