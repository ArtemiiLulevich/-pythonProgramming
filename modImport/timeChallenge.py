import pytz
import datetime
from random import randint
"""
    country = 'Europe/Kiev'
    
    tz_to_displey = pytz.timezone(country)
    local_time = datetime.datetime.now(tz=tz_to_displey)
    
    print("The time in {} is {}".format(country, local_time))
    print("UTC is {}".format(datetime.datetime.utcnow()))
    
    
    countries = pytz.country_timezones
    
    print(countries["UA"])
    #print(list(countries.values()))
"""
timeZonesNum = []
for x in range(9):
    randNum = randint(0, len(pytz.all_timezones))
    if randNum not in timeZonesNum:
        timeZonesNum.append(randNum)
    else:
        timeZonesNum.append(randNum+1)


# for y in timeZonesNum:
#    print(y)

timeZones = dict()
for x in range(0, len(timeZonesNum)):
    timeZones[x+1] = pytz.all_timezones[timeZonesNum[x]]

# for y in timeZones:
#    print(y)

menuStr = '{}: {}'
inputStr = 'Enter number to choose timeZone or 0 to exit...\n'

localTimeStr = "%d/%m/%Y %H:%M:%S %Z%z"

for x in range(1, len(timeZones)+1):
    print(menuStr.format(x, timeZones[x]))
while True:

    inputNum = int(input(inputStr))

    if inputNum == 0:
        print("Good bye...")
        break

    if inputNum in timeZones:
        country = timeZones[inputNum - 1]
        tz_to_display = pytz.timezone(country)
        world_time = datetime.datetime.now(tz=tz_to_display)
        local_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()

        # aware_local_time = pytz.utc.localize(local_time).astimezone()

        print("The time in {} is {} {}".format(country, world_time.strftime(localTimeStr), world_time.tzname()))
    else:
        print("You enter incorrect number Local time is {} ".format(local_time.strftime(localTimeStr)))
