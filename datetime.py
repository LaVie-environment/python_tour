#!/usr/bin/python

from datetime import datetime

import random
import time

odds = [1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
       21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
       41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

#for i in range(3):
right_this_hour = datetime.now().hour
right_this_minute = datetime.now().minute
right_this_second = datetime.now().second

if right_this_minute and right_this_second in odds:
    print("This {} hour, {} minute and {} and second seems a little odd.".format(right_this_hour, right_this_minute, right_this_second))
else:
    print("This {} hours, {} minutes, and {} seconds is not an odd time.".format(right_this_hour, right_this_minute, right_this_second))
wait_time = random.randint(1,60)
time.sleep(wait_time)