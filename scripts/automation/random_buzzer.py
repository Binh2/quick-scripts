import os
import sys
import TimerClass

timer = TimerClass.Timer(90 * 60) # 90 minutes
timer.countdown()

import notify
notify.notify()