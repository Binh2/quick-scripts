from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import clipboard
import time
import argparse

argParser = argparse.ArgumentParser(prog="Search on copy", description="Search on a browser when the clipboard changed")
argParser.add_argument("-p", "--postfix", help="Add a postfix to the search string", default="")
args = argParser.parse_args()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version='114.0.5735.90').install()))
driver.get('https://www.google.com')
copied = clipboard.paste()
while True:
    newCopied = clipboard.paste()
    if copied == newCopied:
        time.sleep(0.2)
    else:
        postfix = (" " if args.postfix else "") + args.postfix
        print(postfix)  
        driver.get("https://www.google.com/search?q=" + newCopied + postfix)
        copied = newCopied