import datetime
mytime=datetime.time(2,40,15,3)
print(mytime.hour)
print(mytime.minute)
print(mytime.second)
print(mytime.microsecond)
print(mytime)
print(datetime.time)
print(datetime.date.today())
print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.today().day)
print(datetime.date.today().ctime())


from datetime import datetime
mydatetime=datetime(2021,12,13,10,15,5,6)
print(mydatetime)

print(mydatetime.replace(year=2022))


from datetime import date
date1 = date(2021,7,26)
date2 = date(1934,5,23)

date3 = date1-date2
print(date3)
print(type(date3))


datetime1=datetime(2022,12,23,14,50,15)
datetime2=datetime(2022,12,23,12,10,25)
datetinediff=datetime1-datetime2
print(datetinediff)




