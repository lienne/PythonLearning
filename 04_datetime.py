import datetime

# dir(datetime)
# help(datetime.date)
# date(year, month, day) --> date object

print('Using date class')

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

print('==============================')

# dir(timedelta)
# Lets you add or subtract a number of days from a date
# A pos num will increase the date, a neg num will decrease it.
print('Using timedelta class')
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(mill + dt)

print('==============================')

# Default format: yyyy-mm-dd
# You can specify a different format, however.
# Day-name, Month-name Day-#, Year
# See full documentation at https://docs.python.org/

print('Formatting date display')
# old way
print(gvr.strftime("%A, %B %d, %Y"))

message = "GVR was born on {:%A, %B %dst, %Y}."
print(message.format(gvr))

print('==============================')

print('Using date, time, and datetime classes')
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0) # args are hours, mins, secs
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0) # both date & time

print('launch_date, launch_time, launch_datetime:')
print(launch_date)
print(launch_time)
print(launch_datetime)

print('launch_time hour, min, sec, microsec:')
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)
print(launch_time.microsecond)

print('launch_datime yr, mon, day, hr, min, sec:')
print(launch_datetime.year)
print(launch_datetime.month)
print(launch_datetime.day)
print(launch_datetime.hour)
print(launch_datetime.minute)
print(launch_datetime.second)

print('==============================')

# Accessing current datetime
# - Module: datetime
# - Class: datetime
# - Method: today()
# in UTC format:

print('Accessing current datetime')
now = datetime.datetime.today()
print(now)
print(now.microsecond)

# Convert Strings to Datimes
# - Module: datetime
# - Class: datetime
# - Method: strptime() <-- abbreviation for 'string parse time'

print('==============================')

print('Converting Strings to Datimes')
moon_landing = "7/20/1969"
# First arg is string containing date, second arg is expected format
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(type(moon_landing_datetime))