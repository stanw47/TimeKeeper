import timeit
print("Glad that you're doing work now, Don't forget to enter this into your Timesheet when you're done!")

import time
import sys

time_start = time.time()
seconds = 0
minutes = 0

while True:
    try:
        sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
        sys.stdout.flush()
        time.sleep(1)
        seconds = int(time.time() - time_start) - minutes * 60
        if seconds >= 60:
            minutes += 1
            seconds = 0
    except KeyboardInterrupt(e):
        break
