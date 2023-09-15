import time
from win10toast import ToastNotifier

def notify():
    toaster = ToastNotifier()
    toaster.show_toast("Time's up",icon_path= 
    "toast.ico",duration=10,threaded=False)
    while toaster.notification_active():
        ime.sleep(0.1)