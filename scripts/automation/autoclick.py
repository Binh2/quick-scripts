import csv
import time
import utilities
import pyautogui

utilities.minimize_window()

with open('cordinates.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for i in range(10):
        csvfile.seek(0)
        for row in reader:
            my_tuple = row[0].split(",")
            if len(my_tuple) == 3:
                x, y, boolean = *my_tuple,
            else:
                x, y = *my_tuple,
                boolean = 0
            x = int(x)
            y = int(y)
            boolean = int(boolean)
            if boolean == 1:
                pyautogui.click(x, y)
            else:
                utilities.click(x, y)
       

time.sleep(100)
