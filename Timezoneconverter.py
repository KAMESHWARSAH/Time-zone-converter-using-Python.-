import pytz, datetime

year = int(input())
month = int(input())
day = int(input())
hour = int(input())
minute = int(input())

#converting to a date

users_time = datetime.datetime(year,month,day,hour,minute)

delhi_timezone = pytz.timezone('Asia/Kolkata')
tokyo_timezone = pytz.timezone('Asia/Tokyo')
london_timezone = pytz.timezone('UTC')
sydney_timezone = pytz.timezone('Australia/Sydney')

bihar_timezone = pytz.timezone('Asia/Kolkata')
mumbai_timezone = pytz.timezone('Asia/Tokyo')
pune_timezone = pytz.timezone('UTC')
punjab_timezone = pytz.timezone('Australia/Sydney')


delhi_time = pytz.utc.localize(users_time).astimezone(delhi_timezone)
tokyo_time = pytz.utc.localize(users_time).astimezone(tokyo_timezone)
london_time = pytz.utc.localize(users_time).astimezone(london_timezone)
sydney_time = pytz.utc.localize(users_time).astimezone(sydney_timezone)

bihar_time = pytz.utc.localize(users_time).astimezone(delhi_timezone)
mumbai_time = pytz.utc.localize(users_time).astimezone(tokyo_timezone)
pune_time = pytz.utc.localize(users_time).astimezone(london_timezone)
punjab_time = pytz.utc.localize(users_time).astimezone(sydney_timezone)

print("New Delhi Time is", delhi_time.isoformat())
print("Tokyo Time is", tokyo_time.isoformat())
print("London Time is", london_time.isoformat())
print("Sydney Time is", sydney_time.isoformat())

print("New Delhi Time is", bihar_time.isoformat())
print("Tokyo Time is", mumbai_time.isoformat())
print("London Time is", pune_time.isoformat())
print("Sydney Time is", punjab_time.isoformat())
