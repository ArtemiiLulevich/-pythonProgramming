# import time

# print(time.gmtime(0))
#
# print(time.localtime())
#
# print(time.time())

# time_here = time.localtime(1453234500)
#
# print("Year", time_here.tm_year, time_here[0])
# print("Month", time_here.tm_mon)

import time
import random
from time import time as my_timer

input("Press enter to stars")

wait_time = random.randint(1, 7)

time.sleep(wait_time)
start_time = my_timer()

input("Press enter to stop")
end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} second".format(end_time - start_time))

help(time)