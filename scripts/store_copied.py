from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import clipboard
import time
import argparse

argParser = argparse.ArgumentParser(prog="Search on copy", description="Search on a browser when the clipboard changed")
argParser.add_argument("-p", "--postfix", help="Add a postfix to the search string", default="")
args = argParser.parse_args()

copied = clipboard.paste()
copies = []
copies.append(copied)
try: 
    while True:
        newCopied = clipboard.paste()
        if copied == newCopied:
            time.sleep(0.2)
        else:
            postfix = (" " if args.postfix else "") + args.postfix
            copies.append(newCopied + postfix)
finally:
    print(copies)
    input()