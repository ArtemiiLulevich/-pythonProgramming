# import time
#
# print("Epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("Time zone {0} - {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDaylight Saving Time is in effect for this location")
#     print("\tThe DST timezone is " + time.tzname[1])
#
# print("Loc time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
#
# for i in time.tzname:
#     print(i)

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())