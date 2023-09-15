from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import sys
import pyperclip
import utilities


def search_if_kanji(searchWhat):
    if utilities.has_cjk(search):
        global driver
        global tabsNum
        if tabsNum == 0:
            driver = webdriver.Firefox(executable_path="C:\cua-Binh\MyPython\geckodriver.exe")
            
       
        else:
            driver.execute_script("window.open();")
            driver.switch_to.window(driver.window_handles[-1])
            
        driver.get("https://www.kanjidamage.com")
        tabsNum += 1
        elem = driver.find_element_by_css_selector("#q")
        elem.click()
        elem.send_keys(utilities.remove_kana(search))
        elem.submit()

if len(sys.argv) > 1:
    search = ''.join(sys.argv[1:])
else:
    search = pyperclip.paste()
    

tabsNum = 0
search_if_kanji(search)

while True:
    try:
        search = pyperclip.waitForNewPaste(1)
    except:
        search = "a"
    search_if_kanji(search)
print("Done!")
