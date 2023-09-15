import time
# import click
import sys, os
import winsound
import toast_notification
import TimerClass

if (len(sys.argv) > 2):
    unit = sys.argv[2]
    my_time = int(float(sys.argv[1]))
    if (unit == "sec" or unit == "secs" or unit == "second" or unit == "seconds" or unit == "s"):
        second = my_time
    elif (unit == "min" or unit == "mins" or unit == "minute" or unit == "minutes" or unit == "m"):
        second = my_time * 60
    elif (unit == "hour" or unit == "hours" or unit == "h"):
        second = my_time * 3600
    else:
        second = my_time * 60
elif (len(sys.argv) == 2):
    my_time = int(float(sys.argv[1]))
    second = my_time * 60
elif (len(sys.argv) < 2):
    second = 60
        
timer = TimerClass.Timer(second)
for i in range(second):
    print(timer.count_down(), flush = True)
    time.sleep(1)
    # click.clear()
    os.system('cls')
                
for i in range(3):
    winsound.Beep(2000, 250)

toast_notification.notify()
