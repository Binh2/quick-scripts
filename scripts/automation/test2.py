import time
print("hello")
time.sleep(1)

import click
click.clear()
import sys


for item in sys.argv[0:]:
    print(item)
time.sleep(100)
