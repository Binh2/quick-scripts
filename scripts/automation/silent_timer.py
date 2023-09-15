import time
import click
import sys
import winsound
import toast_notification

class Timer:
    def __init__(self, second):
        second = int(float(second))
        self._second = second % 60
        self._minute = (second // 60) % 60
        self._hour = second // 3600
        
        
    def clock_string(self):
        if (0 <= self._hour <= 9):
            return_string = "0" + str(self._hour)
        else:
            return_string = str(self._hour)
        
        if (0 <= self._minute <= 9):
            return_string = return_string + ":" + "0" + str(self._minute)
        else:
            return_string = return_string + ":" + str(self._minute)
    
        if (0 <= self._second <= 9):
            return_string = return_string + ":" + "0" + str(self._second)
        else:
            return_string = return_string + ":" + str(self._second)
        return return_string
        
        
    def count_down(self):
        self._second -= 1;
        if (self._second == -1):
            self._second = 59
            self._minute -= 1
            if (self._minute == -1):
                self._minute = 59
                self._hour -= 1
        return self.clock_string()
                

if (len(sys.argv) > 2):
    unit = sys.argv[2]
    my_time = int(float(sys.argv[1]))
    if (unit == "sec" or unit == "secs" or unit == "second" or unit == "seconds"):
        second = my_time
    elif (unit == "min" or unit == "mins" or unit == "minute" or unit == "minutes"):
        second = my_time * 60
    elif (unit == "hour" or unit == "hours"):
        second = my_time * 3600
    else:
        second = my_time * 60
elif (len(sys.argv) == 2):
    my_time = int(float(sys.argv[1]))
    second = my_time * 60
elif (len(sys.argv) < 2):
    second = 60
        
timer = Timer(second)
for i in range(second):
    print(timer.count_down(), flush = True)
    time.sleep(1)
    click.clear()

toast_notification.notify()
