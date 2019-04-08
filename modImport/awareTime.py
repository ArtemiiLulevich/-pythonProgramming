import datetime
import pytz

country = 'America/Nipigon'
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {}". format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))

