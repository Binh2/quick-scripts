import toast_notification
import winsound

def notify():
    for i in range(3):
        winsound.Beep(2000, 250)

    toast_notification.notify()